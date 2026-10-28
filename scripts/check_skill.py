"""Validate local references, rule working-set budgets and adapter preservation.

Run: python scripts/check_skill.py [--base <git revision>]
No API calls or video generation; behavioral cases are documented separately.
"""
from pathlib import Path
import argparse
import re
import subprocess

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / 'skills/storyboard-prompt-optimizer-l5'
WORKING_SET = ['SKILL.md', 'references/production-core.md',
               'references/seedance-2-5-adapter.md']


def section(text, prefix):
    for part in re.split(r'(?=^## )', text, flags=re.M):
        if part.startswith(prefix):
            return part.strip()
    raise AssertionError(f'Missing section: {prefix}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Compare recorded model limits to this revision')
    args = parser.parse_args()
    problems = []
    files = list(ROOT.rglob('*.md'))
    for file in files:
        text = file.read_text(encoding='utf-8')
        if text.count('```') % 2:
            problems.append(f'Unclosed code fence: {file.relative_to(REPO)}')
        # Markdown links plus bare/backticked reference filenames used by old files.
        targets = re.findall(r'\]\(([^)]+)\)', text)
        targets += re.findall(r'(?<![\w/-])(?:references/)?[a-z][a-z0-9-]*\.md', text)
        for target in set(targets):
            if '://' in target or target.startswith('#'):
                continue
            target = target.split('#')[0]
            candidates = [file.parent / target, ROOT / target,
                          ROOT / 'references' / target, REPO / target]
            if not any(p.is_file() for p in candidates):
                problems.append(f'Missing reference: {file.relative_to(REPO)} -> {target}')
    entry = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
    if not re.match(r'\A---\nname: [a-z0-9-]+\ndescription: .+\n---\n', entry):
        problems.append('Invalid skill frontmatter')
    lengths = {name: len((ROOT / name).read_text(encoding='utf-8')) for name in WORKING_SET}
    if sum(lengths.values()) > 15000:
        problems.append('Common working set exceeds 15,000 Unicode characters')
    if args.base:
        adapter_path = 'skills/storyboard-prompt-optimizer-l5/references/seedance-2-5-adapter.md'
        old = subprocess.check_output(['git', 'show', f'{args.base}:{adapter_path}'],
                                      cwd=REPO).decode('utf-8')
        current = (REPO / adapter_path).read_text(encoding='utf-8')
        for heading in ['## 一、', '## 二、', '## 四、', '## 五、', '## 十、']:
            if section(old, heading) != section(current, heading):
                problems.append(f'Recorded adapter contract changed: {heading}')
        # Keep the original official/experience text intact. The reviewed project
        # policy is an explicit appended block, not an exemption for arbitrary edits.
        eye_section = section(current, '## 六、')
        policy_marker = '\n\n项目眼部防护范围（v1.38 补充，项目约定）：'
        original, marker, addition = eye_section.partition(policy_marker)
        if original != section(old, '## 六、'):
            problems.append('Original adapter section VI changed')
        if not marker or not addition.strip() or '\n\n' in addition:
            problems.append('Expected one explicit project eye-protection policy block')
        details = (ROOT / 'references/seedance-special-tasks.md').read_text(encoding='utf-8')
        # The only migration edit is qualifying a reference to the source file.
        details = details.replace('见 seedance-2-5-adapter.md 第五节静默预算', '见第五节静默预算')
        for heading in ['## 三、', '## 七、', '## 八、', '## 九、']:
            if section(old, heading) != section(details, heading):
                problems.append(f'Moved adapter detail changed: {heading}')
    print(f'Markdown files checked: {len(files)}')
    for name, length in lengths.items():
        print(f'{name}: {length} characters')
    print(f'Common working set: {sum(lengths.values())} characters')
    for problem in sorted(set(problems)):
        print(f'FAIL: {problem}')
    if problems:
        raise SystemExit(1)
    print('PASS: references, fences, frontmatter, budget and requested preservation checks')


if __name__ == '__main__':
    main()

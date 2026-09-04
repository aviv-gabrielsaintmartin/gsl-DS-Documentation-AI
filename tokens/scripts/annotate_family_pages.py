#!/usr/bin/env python3
"""
Annotate the colour family pages with real usage, from the generated ledger.

Adds (or refreshes) a **Used by** column on every Semantic usage / Overview
table in background.md, surface.md, border.md and content.md, listing the
components that actually bind each token. Tokens with no consumer are marked
**not used**.

Idempotent: re-running replaces the existing column rather than adding a second
one. Only the guidance tables are touched — the `## Tokens` value tables are
never modified.

Run after `extract_color_usage.py`:
    python3 annotate_family_pages.py            # all four pages, in place
    python3 annotate_family_pages.py --check    # report drift, write nothing
"""
import argparse
import json,re,sys,pathlib
HERE=pathlib.Path(__file__).resolve().parent
LEDGER=HERE.parent/"color"/"color-usage-ledger.json"
PAGES_DIR=HERE.parent/"color"
PAGES=["background.md","surface.md","border.md","content.md"]
L=json.load(open(LEDGER)); T=L["tokens"]

# Component-token files that describe a component with no implementation
# anywhere in the monorepo (see color-usage-audit.md E2). A token whose only
# consumer is one of these is effectively unused.
PHANTOM = {"mapPin", "barChart", "brandLogo", "scoreTag"}

def to_key(name):
    parts=[p for p in name.strip('`').split('/') if p]
    out=[]
    for p in parts:
        segs=p.split('-')
        s=segs[0]+"".join(x[0].upper()+x[1:] for x in segs[1:])
        out.append(s[0].lower()+s[1:])
    return "color."+".".join(out)

def resolve(name):
    k=to_key(name)
    return [t for t in T if t==k or t.startswith(k+".")]

def used_by(name, maxn=4):
    toks=resolve(name)
    if not toks: return None
    comps, dyn, direct = set(), False, set()
    for t in toks:
        comps |= set(T[t]["component_consumers"])
        direct |= set(T[t]["direct_code_owners"])
        if T[t]["dynamic_code_uses"]: dyn=True
    if not comps and not direct and not dyn:
        return "**not used**"
    bits=[]
    cs=sorted(comps)
    names=[f"`{c}`" + (" (no component)" if c in PHANTOM else "") for c in cs[:maxn]]
    bits.append(", ".join(names) + (f" +{len(cs)-maxn}" if len(cs)>maxn else ""))
    if direct: bits.append(f"direct: {', '.join(f'`{d}`' for d in sorted(direct)[:2])}")
    if dyn: bits.append("dynamic")
    return " · ".join(b for b in bits if b)

def strip_column(line):
    """Remove a trailing `Used by` cell so re-runs replace rather than stack."""
    cells=[c for c in line.split("|")]
    if len(cells)>=3 and cells[-1].strip()=="":
        cells=cells[:-1]
    return "|".join(cells[:-1])+"|" if len(cells)>2 else line

def annotate(path):
    txt=open(path).read()
    head, sep, tail = txt.partition("## Tokens")
    lines=head.splitlines()
    out=[]; i=0
    while i < len(lines):
        ln=lines[i]
        m=re.match(r'^\|\s*(Token|Token root|Family)\s*\|', ln)
        if m:
            # find the table block
            j=i; block=[]
            while j<len(lines) and lines[j].startswith("|"):
                block.append(lines[j]); j+=1
            if block[0].rstrip().rstrip("|").rstrip().endswith("Used by"):
                block=[strip_column(b) for b in block]
            rows=block[2:]
            resolvable=sum(1 for r in rows if re.match(r'^\|\s*`([^`]+)`', r) and resolve(re.match(r'^\|\s*`([^`]+)`', r).group(1)))
            if resolvable >= max(1, len(rows)//2):
                out.append(block[0].rstrip().rstrip('|')+"| Used by |")
                out.append(block[1].rstrip().rstrip('|')+"| --- |")
                for r in rows:
                    mm=re.match(r'^\|\s*`([^`]+)`', r)
                    u=used_by(mm.group(1)) if mm else None
                    if u is None:  # a group heading, not a token
                        u="see below"
                    out.append(r.rstrip().rstrip('|')+f"| {u} |")
            else:
                out.extend(block)
            i=j; continue
        out.append(ln); i+=1
    return "\n".join(out)+"\n"+sep+tail

def main():
    ap=argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="report which pages would change; write nothing")
    ap.add_argument("pages", nargs="*", default=None,
                    help="pages to annotate (default: all four)")
    a=ap.parse_args()
    base=PAGES_DIR
    changed=[]
    for name in (a.pages or PAGES):
        p=base/name
        new=annotate(str(p))
        if new != p.read_text():
            changed.append(name)
            if not a.check: p.write_text(new)
    if a.check:
        print("would change:", ", ".join(changed) or "nothing — pages are current")
    else:
        print("updated:", ", ".join(changed) or "nothing — already current")

if __name__=="__main__":
    main()

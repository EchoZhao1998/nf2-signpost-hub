# MediPort Signpost — NF2-SWN resource hub (prototype)

A small, accessible "signpost" that helps people affected by NF2-related schwannomatosis (NF2-SWN) find trusted resources that already exist, filtered by:

1. **Who you are**: living with NF2, a carer, a clinician, or an employer/teacher
2. **What you need help with**: diagnosis → just diagnosed → specialist care → treatment decisions → hearing & communication → daily life → research & trials
3. **Where you live**: Australia, UK, US, Malaysia, plus international resources

Part of the MediPort UX case study (Monash University / PwC project, 2026).

## Why a signpost, not a library

NF2IS, the Children's Tumor Foundation, Nerve Tumours UK, CTF Australia, NHS centres and others already publish good content. The problem we're solving is **finding the right piece for your situation**, not writing new content. So the hub links out, uses its own short summaries, and shows when each link was last checked.

## Accessibility choices

- **Atkinson Hyperlegible** font, high contrast, large tap targets, visible focus outlines
- A **"Works without hearing"** filter, because hearing loss is common in NF2-SWN
- **"Copy this list"** so carers can paste a shortlist into a message
- Chip filters are real buttons with `aria-pressed`; results count is announced with `aria-live`

## Run it

Open `index.html` in a browser. No server or install needed.

## Update the data

1. Edit `data/resources.json` (exported from the NF2-SWN Resource Map sheet)
2. Run `python3 build.py` to regenerate `index.html`

## Publish on GitHub Pages

Settings → Pages → Deploy from branch → `main` / root.

## Disclaimer

Not medical advice. All linked content belongs to its publishers.

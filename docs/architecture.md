# Project Structure

VELA does not require a hidden database. A project should be readable as files and folders.

## Suggested Shape

```text
my-research-project/
  materials/
  evidence/
  claims/
  methods/
  deliverables/
  handoffs/
```

## What To Keep Private

Keep raw private data, credentials, account traces, personal notes, and restricted source material inside your own project storage. Do not place them in a public copy of VELA.

## What HELM Reads

If you use HELM, it should read the project state you already maintain. HELM is a view over the work, not the only place where the work exists.

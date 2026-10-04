---
id: P13
url: /software/raqib
canonical: https://cybertronix.tech/software/raqib
title: "Raqib: Terminal Monitor for AI Workloads · Cybertronix"
description: "Raqib is a terminal app with a local web view that watches AI workloads: RAM, CPU load, VRAM, temperatures and top processes. Early build by Cybertronix."
eyebrow: "Raqib · terminal monitor for AI workloads · early build"
h1: "See what your AI is really using."
keyword: "AI workload monitor · VRAM monitor for local LLMs · terminal system monitor for AI · Raqib"
schema: [SoftwareApplication, FAQPage, BreadcrumbList]
---

> Build note (D30, D31): describe **only what the reference screenshot shows**
> (`docs/reference/raqib-tui-current.png`). Status label: "Early build".
> - `SoftwareApplication`: `name` "Raqib", `applicationCategory` "DeveloperApplication", `creator` =
>   Organization. **No `offers`, `operatingSystem`, `downloadUrl`, `softwareVersion` or ratings** until
>   the founder gives them (`TODO(founder)`).
> - ⚠ The screenshot's title bar shows a username and hostname. Don't publish the raw screenshot. Use
>   Design's R2 redesign, or crop/blur the title bar first.
> - Brand: "Raqib" alone is used by several other products (raqib.ai, withraqib.com, a GitHub website
>   monitor). Always pair it: "Raqib by Cybertronix" or "Raqib AI workload monitor".

## P13.1 Hero

Raqib · terminal monitor for AI workloads · early build

# See what your AI is really using.

**Early build**

Running AI models on your own machine? Raqib is a terminal monitor for AI workloads: one screen shows how
much RAM, CPU and VRAM they're using, how hot the machine is running, and which processes are using the
most. A local web view shows it in your browser too.

**CTA:** `TODO(founder)`: download, GitHub or "Get notified". Until then: Ask about Raqib → /contact

## P13.2 What Raqib shows

| Panel | What you see |
|---|---|
| Vitals | RAM in use, CPU load (three load averages) and CPU count, VRAM in use and number of GPU devices, total processes, and temperatures from the machine's thermal sensors |
| AI workloads | The AI workloads Raqib detects on the machine, with a count at the top of the screen, including how many are degraded |
| Top processes by RAM | The five processes using the most memory |
| Top processes by VRAM | The five processes using the most GPU memory |
| Top processes by CPU | The five busiest processes, by CPU % per core |
| Activity | Recent events |

> Build note: each row is visible in the reference screenshot. Don't add rows (alerts, logs export,
> remote machines, model names and so on) unless the founder confirms them.

## P13.3 Keyboard first

Raqib runs in the terminal and is driven from the keyboard:

| Key | Action |
|---|---|
| `j` / `k` | Select a row |
| `k` | Kill a process, with a confirmation step |
| `h` | History |
| `?` | Help |
| `q` | Quit |

> Build note: the screenshot's footer shows `k` for kill and "j/k" for select. Keep the table exactly as
> the app shows it. `TODO(founder)`: confirm how `k` works in each mode.

## P13.4 Local web view

While Raqib runs, it also serves a web view on your own machine at `http://localhost:7070`, so you can
keep an eye on it in a browser tab.

> Build note: Design's R3 board shows this view. Use that, not an invented screenshot.

## P13.5 Why we built it

`TODO(founder)`: one or two lines in your own words on why the team built Raqib. Hidden until answered.

## P13.6 Status and availability

Raqib is an early build.

`TODO(founder)`: supported operating systems and GPUs, how to install, licence (free, open source,
paid?), and where to get it. Hidden until answered.

## P13.7 Questions about Raqib

### What is Raqib?
A terminal app by Cybertronix that monitors AI workloads on a machine: RAM, CPU load, VRAM,
temperatures, AI processes and the top processes by memory, GPU memory and CPU.

### Can Raqib show VRAM usage for local LLMs?
It shows VRAM in use across the machine's GPU devices and lists the top processes by VRAM, so you can see
what a model is using. `TODO(founder)`: confirm it detects local LLM runners (for example Ollama) as AI
workloads before naming any.

### Does Raqib have a web dashboard?
Yes. While it runs, it serves a local web view at `http://localhost:7070`.

### Can I stop a process from Raqib?
Yes. Select it and press `k`. Raqib asks you to confirm before it kills the process.

### Is Raqib free, and which systems does it run on?
`TODO(founder)`. Hidden until answered.

## P13.8 Follow Raqib

**CTA:** `TODO(founder)`: download / GitHub / "Get notified". Fallback: Ask about Raqib → /contact

Related: [All software](/software) · [AI vision](/ai-vision) · [Our team](/team)

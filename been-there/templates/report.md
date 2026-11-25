# Visual report template

When the user accepts the visual report, copy the HTML below into a new `.html` file, replace **only** the JSON inside `<script id="REPORT_DATA">` with this decision's data (same keys), and deliver the file (or publish it as an artifact). Keep everything else unchanged.

Keys: `title`, `date`, `verdict`, `confidence` (0–10), `agreement`, `disagreement`, `key_assumption`, `precedents[]` (`type` failure|survivor, `name`, `years`, `note`, `match[]`, `miss[]`), `advisors[]` (`name`, `position` for|against|depends, `line`, `opinion` true|false), `premortem[]`, `next_step`, `kill_criterion`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Been There · Report</title>
<style>
  :root{--bg:#f6f3ee;--card:#fff;--ink:#1d1b18;--muted:#756f66;--line:#e6e0d7;--for:#2f8f5b;--against:#c8442f;--depends:#c89a2f;--accent:#1d1b18}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif;padding:28px 16px 60px}
  .wrap{max-width:760px;margin:0 auto;display:flex;flex-direction:column;gap:22px}
  .eyebrow{font:600 12px/1 ui-monospace,Menlo,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
  h1{font-size:clamp(24px,5vw,34px);line-height:1.15;margin:6px 0 0}
  h2{font-size:15px;text-transform:uppercase;letter-spacing:.06em;margin:0 0 10px;color:var(--muted)}
  .card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
  .verdict{display:flex;gap:18px;align-items:center;flex-wrap:wrap}
  .verdict strong{font-size:22px;flex:1;min-width:220px}
  .conf{display:flex;flex-direction:column;align-items:center;min-width:90px}
  .conf b{font-size:34px;line-height:1}
  .bar{width:90px;height:6px;border-radius:3px;background:var(--line);overflow:hidden;margin-top:6px}
  .bar i{display:block;height:100%;background:var(--accent)}
  .grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
  @media(max-width:600px){.grid2{grid-template-columns:1fr}}
  .prec{display:flex;flex-direction:column;gap:10px}
  .p{display:grid;grid-template-columns:28px 1fr;gap:10px;align-items:start}
  .p .ic{width:28px;height:28px;border-radius:8px;display:grid;place-items:center;font-size:15px;color:#fff}
  .p.failure .ic{background:var(--against)} .p.survivor .ic{background:var(--for)}
  .p small{display:block;color:var(--muted)}
  .tags span{display:inline-block;font-size:12px;border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin:4px 4px 0 0}
  .tags .miss{opacity:.45;text-decoration:line-through}
  table{width:100%;border-collapse:collapse;font-size:15px}
  td{padding:9px 6px;border-top:1px solid var(--line);vertical-align:top}
  tr:first-child td{border-top:0}
  .pos{font-weight:700;font-size:12px;text-transform:uppercase;padding:2px 8px;border-radius:999px;color:#fff;white-space:nowrap}
  .pos.for{background:var(--for)} .pos.against{background:var(--against)} .pos.depends{background:var(--depends)}
  .op{font-size:12px;color:var(--muted);font-style:italic}
  ol{margin:0;padding-left:20px} li{margin:4px 0}
  .kv{display:grid;grid-template-columns:auto 1fr;gap:6px 14px}
  .kv dt{font-weight:700} .kv dd{margin:0}
  footer{color:var(--muted);font-size:13px;text-align:center}
</style>
</head>
<body>
<div class="wrap" id="app"></div>

<!-- Replace only this JSON when generating a report. -->
<script id="REPORT_DATA" type="application/json">
{
  "title": "Example: launch same-day grocery delivery in 8 cities at once?",
  "date": "2026-11-24",
  "verdict": "First prove one city, then expand",
  "confidence": 8,
  "agreement": "Volume won't fix negative per-order margins; it multiplies them.",
  "disagreement": "Expansionist argues speed matters against competitors; others say speed without economics is how Webvan died.",
  "key_assumption": "Per-order loss drops below zero with density → test with 4 weeks of route data in city 1.",
  "precedents": [
    {"type":"failure","name":"Webvan","years":"1996–2001","note":"Built warehouses in many cities before one was profitable.","match":["market","mechanism"],"miss":["timing"]},
    {"type":"survivor","name":"Instacart","years":"2012–","note":"Same trap, asset-light: picked from existing stores.","match":["market","model"],"miss":[]}
  ],
  "advisors": [
    {"name":"Devil's advocate","position":"against","line":"You're Webvan with better branding: losses scale with cities.","opinion":false},
    {"name":"First principles","position":"depends","line":"The goal is density per route, not number of cities.","opinion":false},
    {"name":"Expansionist","position":"for","line":"First mover in 8 cities could lock in partnerships.","opinion":true},
    {"name":"Outsider","position":"depends","line":"Why would I switch from my current delivery app?","opinion":true},
    {"name":"Executor","position":"against","line":"Tomorrow: measure cost per order by route, not average.","opinion":false}
  ],
  "premortem": [
    "Per-order losses grew with each new city (signal: contribution margin by city).",
    "Warehouse capex locked cash before demand was proven (signal: utilisation < 40%).",
    "Competitor with no warehouses undercut prices (signal: Instacart-style partner model in your market)."
  ],
  "next_step": "Pull 4 weeks of order data in city 1 and compute margin per route density.",
  "kill_criterion": "If margin per order isn't positive at the best-density routes by 31 Jan, stop expansion plans."
}
</script>

<script>
  const d = JSON.parse(document.getElementById('REPORT_DATA').textContent);
  const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const posLabel = {for:'For', against:'Against', depends:'Depends'};
  document.title = 'Been There · ' + d.title;
  document.getElementById('app').innerHTML = `
    <header>
      <div class="eyebrow">Been There · ${esc(d.date)}</div>
      <h1>${esc(d.title)}</h1>
    </header>

    <section class="card verdict">
      <strong>${esc(d.verdict)}</strong>
      <div class="conf"><b>${esc(d.confidence)}<span style="font-size:16px">/10</span></b>
        <div class="bar"><i style="width:${Math.max(0,Math.min(10,+d.confidence))*10}%"></i></div>
        <span class="eyebrow" style="margin-top:6px">confidence</span></div>
    </section>

    <div class="grid2">
      <section class="card"><h2>Agreement</h2>${esc(d.agreement)}</section>
      <section class="card"><h2>Real disagreement</h2>${esc(d.disagreement)}</section>
    </div>

    <section class="card"><h2>Precedents</h2><div class="prec">
      ${(d.precedents||[]).map(p => `
        <div class="p ${p.type==='survivor'?'survivor':'failure'}">
          <div class="ic">${p.type==='survivor'?'✓':'✕'}</div>
          <div><b>${esc(p.name)}</b> <small style="display:inline">${esc(p.years)}</small>
            <small>${esc(p.note)}</small>
            <div class="tags">${(p.match||[]).map(m=>`<span>${esc(m)}</span>`).join('')}${(p.miss||[]).map(m=>`<span class="miss">${esc(m)}</span>`).join('')}</div>
          </div>
        </div>`).join('') || '<em>No strong precedent found.</em>'}
    </div></section>

    <section class="card"><h2>The panel</h2><table>
      ${(d.advisors||[]).map(a => `<tr>
        <td style="width:34%"><b>${esc(a.name)}</b></td>
        <td style="width:1%"><span class="pos ${esc(a.position)}">${esc(posLabel[a.position]||a.position)}</span></td>
        <td>${esc(a.line)} ${a.opinion?'<span class="op">(opinion)</span>':''}</td></tr>`).join('')}
    </table></section>

    <section class="card"><h2>Pre-mortem · 12 months later it failed because…</h2>
      <ol>${(d.premortem||[]).map(x=>`<li>${esc(x)}</li>`).join('')}</ol></section>

    <section class="card"><h2>What to do</h2><dl class="kv">
      <dt>Assumption to test</dt><dd>${esc(d.key_assumption)}</dd>
      <dt>Next 48 h</dt><dd>${esc(d.next_step)}</dd>
      <dt>Kill criterion</dt><dd>${esc(d.kill_criterion)}</dd>
    </dl></section>

    <footer>Generated with Been There · precedents are illustrative, not predictions</footer>`;
</script>
</body>
</html>
```

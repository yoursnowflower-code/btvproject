[index.html](https://github.com/user-attachments/files/31769801/index.html)
<!doctype html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>B tv 프로젝트 대시보드</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Sora:wght@400;500;600;700;800&display=swap">
<style>
  :root{
    --bg:#F7F7FB; --surface:#FFFFFF; --surface-2:#F1F1F6; --surface-3:#E9E8F1;
    --ink:#1C1B29; --ink-soft:#5B596E; --ink-faint:#9694A5;
    --border:#E3E2EC; --border-strong:#CFCDDC;
    --accent:#584BDB; --accent-strong:#443AB0; --accent-soft:#EDEBFA; --accent-contrast:#FFFFFF;
    --st-new:#4757C9; --st-new-soft:#E9EBF9;
    --st-received:#7C4FCC; --st-received-soft:#EFE7FA;
    --st-review:#B4790A; --st-review-soft:#F6EBD5;
    --st-progress:#1D8F5E; --st-progress-soft:#DFF1E7;
    --st-drop:#BD3E52; --st-drop-soft:#F5E3E6;
    --st-tech:#0C7489; --st-tech-soft:#DCEEF1;
    --coral-soft:#FBEAE6; --coral-border:#EEC1B6; --coral-strong:#B14A32;
    --shadow:0 1px 2px rgba(20,16,40,.04), 0 12px 28px -16px rgba(20,16,40,.14);
    --radius-s:7px; --radius-m:12px; --radius-l:18px;
    --font-body:'IBM Plex Sans KR','Noto Sans KR',system-ui,-apple-system,sans-serif;
    --font-mono:'IBM Plex Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
    --font-display:'Sora','IBM Plex Sans KR',system-ui,sans-serif;
  }
  @media (prefers-color-scheme: dark){
    :root:not([data-theme="light"]){
      --bg:#131220; --surface:#191828; --surface-2:#201F31; --surface-3:#28273A;
      --ink:#EDECF3; --ink-soft:#ACA9BF; --ink-faint:#726F87;
      --border:#2B2A3C; --border-strong:#3B394F;
      --accent:#9186FF; --accent-strong:#AFA5FF; --accent-soft:#221F3B; --accent-contrast:#14122A;
      --st-new:#8F9AF5; --st-new-soft:#232647;
      --st-received:#C6A2F2; --st-received-soft:#2B2440;
      --st-review:#E3AE55; --st-review-soft:#392C13;
      --st-progress:#5FD79C; --st-progress-soft:#123423;
      --st-drop:#F1899A; --st-drop-soft:#3A2027;
      --st-tech:#5FC8DA; --st-tech-soft:#123138;
      --coral-soft:#3A241D; --coral-border:#5C3A2C; --coral-strong:#E8967A;
      --shadow:0 1px 2px rgba(0,0,0,.45), 0 14px 30px -18px rgba(0,0,0,.6);
    }
  }
  :root[data-theme="dark"]{
    --bg:#131220; --surface:#191828; --surface-2:#201F31; --surface-3:#28273A;
    --ink:#EDECF3; --ink-soft:#ACA9BF; --ink-faint:#726F87;
    --border:#2B2A3C; --border-strong:#3B394F;
    --accent:#9186FF; --accent-strong:#AFA5FF; --accent-soft:#221F3B; --accent-contrast:#14122A;
    --st-new:#8F9AF5; --st-new-soft:#232647;
    --st-received:#C6A2F2; --st-received-soft:#2B2440;
    --st-review:#E3AE55; --st-review-soft:#392C13;
    --st-progress:#5FD79C; --st-progress-soft:#123423;
    --st-drop:#F1899A; --st-drop-soft:#3A2027;
    --st-tech:#5FC8DA; --st-tech-soft:#123138;
    --coral-soft:#3A241D; --coral-border:#5C3A2C; --coral-strong:#E8967A;
    --shadow:0 1px 2px rgba(0,0,0,.45), 0 14px 30px -18px rgba(0,0,0,.6);
  }

  *{box-sizing:border-box;}
  html,body{margin:0;}
  [hidden]{display:none !important;}
  body{
    background:var(--bg); color:var(--ink); font-family:var(--font-body);
    font-size:14px; line-height:1.5; -webkit-font-smoothing:antialiased;
  }
  ::selection{background:var(--accent-soft); color:var(--accent-strong);}
  a{color:var(--accent-strong);}
  .mono{font-family:var(--font-mono); font-variant-numeric:tabular-nums;}
  button{font-family:inherit;}
  :focus-visible{outline:2px solid var(--accent); outline-offset:2px;}

  .app{max-width:1360px; margin:0 auto; padding:20px 24px 80px;}

  /* ---------- Topbar ---------- */
  .topbar{
    display:flex; flex-wrap:wrap; gap:16px 28px; align-items:flex-end; justify-content:space-between;
    padding:22px 26px; margin-bottom:22px;
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-l);
    box-shadow:var(--shadow);
  }
  .topbar h1{
    margin:0 0 4px; font-size:22px; font-weight:700; letter-spacing:-.01em; text-wrap:balance;
    display:flex; align-items:center; gap:10px;
  }
  .topbar .brand-dot{width:10px; height:10px; border-radius:50%; background:var(--accent); box-shadow:0 0 0 4px var(--accent-soft); flex:none;}
  .topbar .sub{color:var(--ink-soft); font-size:13px;}
  .topbar .sub .sub-accent{color:var(--coral-strong); font-weight:400;}
  .topbar .sub b{color:var(--ink); font-weight:600;}
  .header-actions{display:flex; flex-direction:column; gap:8px; align-items:flex-end; flex:none;}
  .next-up-bar-slot{margin-bottom:22px;}

  /* ---------- 다음 마일스톤 / 다음 배포 하이라이트 카드 ---------- */
  .next-up-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(230px,1fr)); gap:14px; margin-bottom:22px;}
  .next-up-card{border-radius:var(--radius-m); padding:18px 18px 16px; box-shadow:var(--shadow);}
  .next-up-card.milestone{background:linear-gradient(155deg,var(--coral-soft),var(--surface) 75%); border:1px solid var(--coral-border);}
  .next-up-card.deploy{background:linear-gradient(155deg,var(--accent-soft),var(--surface) 75%); border:1px solid var(--accent);}
  .next-up-card .icon{width:24px; height:24px; margin-bottom:10px; opacity:.85; display:block;}
  .next-up-card.milestone .icon{color:var(--coral-strong);}
  .next-up-card.deploy .icon{color:var(--accent-strong);}
  .next-up-card .label{font-size:11px; font-weight:700; color:var(--ink-faint); text-transform:uppercase; letter-spacing:.04em; margin-bottom:4px;}
  .next-up-card .desc{font-size:12.5px; color:var(--ink-soft); margin-bottom:10px; line-height:1.4;}
  .next-up-card .date{font-family:var(--font-display); font-size:16px; font-weight:700;}
  .next-up-card.milestone .date{color:var(--coral-strong);}
  .next-up-card.deploy .date{color:var(--accent-strong);}

  /* ---------- Section shell ---------- */
  section{margin-bottom:30px;}
  section.section-divider{margin-top:34px; padding-top:30px; border-top:1px solid var(--border);}
  .section-head{display:flex; align-items:flex-end; justify-content:space-between; gap:16px; margin-bottom:12px; flex-wrap:wrap;}
  .section-head .eyebrow{
    font-size:11px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; color:var(--accent-strong);
  }
  .section-head h2{margin:2px 0 0; font-size:17px; font-weight:700; letter-spacing:-.01em;}
  .section-head .note{font-size:12.5px; color:var(--ink-faint); max-width:46ch; text-align:right;}
  .section-head .note-link{
    font-size:12.5px; color:var(--accent-strong); font-weight:600; text-decoration:none;
    display:inline-flex; align-items:center; gap:4px;
  }
  .section-head .note-link:hover{text-decoration:underline;}
  .section-head .note-link svg{width:12px; height:12px; flex:none;}

  /* ---------- Stat strip ---------- */
  .stats{display:grid; grid-template-columns:repeat(6,1fr); gap:12px;}
  .stat{
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-m);
    padding:14px 16px; box-shadow:var(--shadow); position:relative; overflow:hidden;
  }
  .stat .n{font-family:var(--font-mono); font-size:26px; font-weight:600; line-height:1;}
  .stat .l{margin-top:6px; font-size:15px; font-weight:700; color:var(--ink);}
  .stat.accent{background:linear-gradient(155deg,var(--accent-soft),var(--surface) 70%);}
  .stat.accent .n{color:var(--accent-strong);}
  .stat .l small{display:block; color:var(--ink-faint); margin-top:2px; font-size:11px; font-weight:400;}
  .stat[data-tile-key="review"] .l{color:var(--st-review);}
  .stat[data-tile-key="progress"] .l{color:var(--st-progress);}
  .stat[data-tile-key="received"] .l{color:var(--st-received);}
  .stat[data-tile-key="new"] .l{color:var(--st-new);}
  .stat[data-tile-key="drop"] .l{color:var(--st-drop);}
  .stat.clickable{cursor:pointer; transition:border-color .12s ease, transform .12s ease, box-shadow .12s ease;}
  .stat.clickable:hover{border-color:var(--border-strong); transform:translateY(-1px);}
  .stat.clickable.active{border-color:var(--accent); box-shadow:0 0 0 2px var(--accent-soft), var(--shadow);}
  .stat.clickable.active .n{color:var(--accent-strong);}
  .stat.clickable::after{
    content:"일감 목록 보기 →"; position:absolute; right:14px; bottom:10px; font-size:10px; color:var(--ink-faint);
    opacity:0; transition:opacity .12s ease;
  }
  .stat.clickable:hover::after{opacity:1;}

  .filter-chip{
    display:inline-flex; align-items:center; gap:8px; font-size:12px; font-weight:500; color:var(--accent-strong);
    background:var(--accent-soft); border:1px solid var(--accent); padding:6px 8px 6px 12px; border-radius:100px;
  }
  .filter-chip button{
    width:18px; height:18px; border-radius:50%; border:none; background:var(--accent); color:var(--accent-contrast);
    cursor:pointer; font-size:10px; line-height:1; display:flex; align-items:center; justify-content:center;
  }
  .filter-chip button:hover{background:var(--accent-strong);}

  /* ---------- Runway ---------- */
  .runway-card{background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-l); box-shadow:var(--shadow); padding:18px 18px 14px;}
  .stage-badge{font-size:10px; font-weight:600; padding:2px 9px; border-radius:100px; white-space:nowrap;}
  .ms-bar.is-current, .ms-dot.is-current{outline:2px solid var(--ink); outline-offset:1px; z-index:4;}
  .ms-bar.is-past{opacity:.4; filter:saturate(.7);}
  .ms-dot.is-past{opacity:.35;}
  .ms-bar.is-past:hover, .ms-dot.is-past:hover{opacity:.7;}
  .runway-legend{display:flex; gap:14px; flex-wrap:wrap; margin-bottom:12px; font-size:12px; color:var(--ink-soft);}
  .runway-legend .lg{display:flex; align-items:center; gap:6px;}
  .runway-legend .sw{width:11px; height:11px; border-radius:3px; flex:none;}
  /* Frozen label column + separately-scrolling timeline, instead of a sticky label
     inside the scrolling row: sticky-inside-flex-inside-horizontal-scroll is fragile
     on mobile webviews (the label could drift and render under the milestone bars
     during scroll), and this also fixes a latent bug where the today-line's percent
     offset was computed against the label+track combined width while every milestone
     bar's percent offset was computed against the track alone — now both share the
     same coordinate space since the label column isn't part of #runwayInner at all. */
  .runway-body{display:flex; align-items:flex-start; border:1px solid var(--border); border-radius:var(--radius-s); overflow:hidden;}
  .runway-labels{flex:none; width:224px; display:flex; flex-direction:column; background:var(--surface); border-right:1px solid var(--border);}
  .runway-labels-spacer{height:22px; border-bottom:1px solid var(--border); flex:none;}
  .runway-scroll{flex:1; min-width:0; overflow-x:auto; overflow-y:hidden; position:relative;}
  .runway-inner{position:relative; min-width:1380px;}
  .runway-months{display:flex; position:relative; height:22px; border-bottom:1px solid var(--border);}
  .runway-month{position:absolute; top:0; height:100%; border-left:1px solid var(--border); font-size:10.5px; color:var(--ink-faint); padding-left:5px; font-family:var(--font-mono);}
  .runway-lane{border-top:1px solid var(--border);}
  .runway-lane:first-child{border-top:none;}
  .lane-label{
    display:flex; flex-direction:column; justify-content:center; gap:4px;
    padding:10px 14px 10px 4px; min-height:44px; border-top:1px solid var(--border);
  }
  .lane-label:first-child{border-top:none;}
  .lane-label-top{display:flex; align-items:center; gap:7px; flex-wrap:wrap;}
  .lane-label-top b{font-family:var(--font-mono); font-size:13px;}
  .lane-label-stage{font-size:11.5px; font-weight:600; color:var(--ink); line-height:1.35; text-wrap:balance;}
  .lane-label-date{font-size:10px; color:var(--ink-faint); font-family:var(--font-mono);}
  .lane-track{position:relative; min-height:44px; padding:6px 0;}
  .today-line{position:absolute; top:0; bottom:0; width:0; border-left:1.5px dashed var(--st-review); z-index:3; pointer-events:none;}
  .today-tag{
    position:absolute; top:-20px; transform:translateX(-50%); font-family:var(--font-mono); font-size:10px;
    background:var(--st-review); color:#231702; padding:1px 6px; border-radius:4px; white-space:nowrap; font-weight:600;
  }
  .ms-bar{
    position:absolute; height:16px; border-radius:5px; cursor:pointer; box-shadow:0 1px 2px rgba(0,0,0,.15);
    display:flex; align-items:center; padding:0 6px; font-size:10px; color:var(--accent-contrast);
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis; min-width:10px; transition:filter .12s ease, transform .12s ease;
    box-sizing:border-box; border:1.5px solid transparent;
  }
  .ms-bar.no-label{padding:0;}
  .ms-bar:hover{filter:brightness(1.08); transform:translateY(-1px); z-index:5;}
  .ms-bar.warn-flag::after{content:"⚠"; margin-left:4px;}
  .ms-bar.is-upcoming{border-style:dashed; box-shadow:none;}
  .ms-dot{
    position:absolute; width:12px; height:12px; border-radius:50%; cursor:pointer; box-shadow:0 1px 2px rgba(0,0,0,.2);
    transition:transform .12s ease; box-sizing:border-box; border:1.5px solid transparent;
  }
  .ms-dot:hover{transform:scale(1.3); z-index:5;}
  .ms-dot.is-upcoming{border-style:dashed; box-shadow:none;}

  /* ---------- Release cards ---------- */
  .release-grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:14px; align-items:start;}
  .release-card{
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-m); padding:15px 16px;
    box-shadow:var(--shadow); display:flex; flex-direction:column; gap:11px; height:346px;
  }
  .release-top{display:flex; justify-content:space-between; align-items:flex-start; gap:8px;}
  .release-ver-header{display:flex; flex-direction:column; gap:4px; padding-bottom:10px; border-bottom:1px dashed var(--border);}
  .release-ver{font-family:var(--font-mono); font-weight:700; font-size:15px;}
  .release-ver-summary{font-size:11.5px; color:var(--ink-soft); line-height:1.5; min-height:33px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;}
  .release-grp{font-size:11.5px; color:var(--ink-faint);}
  .badge{
    display:inline-flex; align-items:center; gap:5px; font-size:11px; font-weight:600; padding:3px 9px;
    border-radius:100px; white-space:nowrap; line-height:1.4;
  }
  .release-meta{font-size:12px; color:var(--ink-soft); display:flex; flex-direction:column; gap:3px;}
  .release-meta b{color:var(--ink); font-weight:600;}
  .release-summary{font-size:12.5px; color:var(--ink-soft); border-top:1px dashed var(--border); padding-top:8px; margin-top:2px;}
  .muted-italic{color:var(--ink-faint); font-style:italic;}
  .release-shared-meta{display:flex; flex-direction:column; gap:6px; padding-bottom:10px; border-bottom:1px dashed var(--border);}
  .release-shared-count{font-size:11.5px; color:var(--ink-soft);}
  .release-shared-count b{color:var(--ink); font-weight:600;}
  .release-shared-count.clickable{
    cursor:pointer; display:inline-flex; align-items:center; gap:3px; width:fit-content;
    margin:-3px -7px; padding:3px 7px; border-radius:100px; transition:background .12s ease, color .12s ease;
  }
  .release-shared-count.clickable::after{content:"›"; font-weight:700; opacity:.6;}
  .release-shared-count.clickable:hover, .release-shared-count.clickable:focus-visible{
    background:var(--accent-soft); color:var(--accent-strong); outline:none;
  }
  .release-shared-count.clickable:hover b, .release-shared-count.clickable:focus-visible b{color:var(--accent-strong);}
  .release-summary-shared{font-size:12.5px; color:var(--ink-soft); line-height:1.45; min-height:36px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;}

  .release-carousel-wrap{position:relative;}
  .release-group-carousel{
    display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scroll-behavior:smooth;
    -webkit-overflow-scrolling:touch; scrollbar-width:none; border-radius:var(--radius-s);
  }
  .release-group-carousel::-webkit-scrollbar{display:none;}
  .release-group-row{
    flex:0 0 100%; scroll-snap-align:start; box-sizing:border-box;
    border:1px solid var(--border); border-radius:var(--radius-s); padding:9px 10px; cursor:pointer;
    display:flex; flex-direction:column; gap:6px; transition:border-color .12s ease, background-color .12s ease;
    background:var(--surface-2);
  }
  .release-group-row:hover{border-color:var(--border-strong); background:var(--surface-3);}
  .release-carousel-nav{
    position:absolute; top:50%; transform:translateY(-50%); width:24px; height:24px; border-radius:50%;
    display:flex; align-items:center; justify-content:center; padding:0; cursor:pointer; z-index:2;
    background:var(--surface); border:1px solid var(--border-strong); color:var(--ink-soft); box-shadow:var(--shadow);
    transition:opacity .12s ease, background-color .12s ease, color .12s ease;
  }
  .release-carousel-nav:hover{background:var(--accent); border-color:var(--accent); color:var(--accent-contrast);}
  .release-carousel-nav svg{width:14px; height:14px;}
  .release-carousel-nav.prev{left:-10px;}
  .release-carousel-nav.next{right:-10px;}
  .release-carousel-nav:disabled{opacity:0; pointer-events:none;}
  .release-group-dots{display:flex; justify-content:center; gap:5px; margin-top:-2px;}
  .release-group-dot{width:6px; height:6px; border-radius:50%; background:var(--border-strong); border:none; padding:0; cursor:pointer; transition:width .15s ease, border-radius .15s ease, background-color .15s ease;}
  .release-group-dot.active{background:var(--accent-strong); width:14px; border-radius:4px;}
  .rg-top{display:flex; justify-content:space-between; align-items:center; gap:8px;}
  .rg-left{display:flex; flex-direction:column; gap:2px; min-width:0;}
  .rg-group{font-size:12.5px; font-weight:700; color:var(--ink);}
  .rg-devices{font-size:11px; color:var(--ink-faint); overflow:hidden; text-overflow:ellipsis; white-space:nowrap;}
  .rg-meta{font-size:11.5px; color:var(--ink-soft); display:flex; flex-wrap:wrap; gap:4px 10px;}
  .rg-meta b{color:var(--ink); font-weight:600;}
  .rg-coverage{margin-top:6px; min-height:45px;}
  .rg-coverage-head{display:flex; justify-content:space-between; align-items:baseline; font-size:11px; color:var(--ink-soft); margin-bottom:3px; gap:8px;}
  .rg-coverage-head .pct{font-family:var(--font-mono); font-weight:700; color:var(--ink); flex:none;}
  .rg-coverage-head .pct.na{color:var(--ink-faint); font-weight:500;}
  .rg-coverage-track{height:6px; background:var(--surface-2); border-radius:100px; overflow:hidden;}
  .rg-coverage-fill{height:100%; background:var(--accent); border-radius:100px;}
  .rg-coverage-foot{font-size:10.5px; color:var(--ink-faint); margin-top:3px; font-family:var(--font-mono);}
  .src-note{font-family:var(--font-body); font-size:10.5px; color:var(--ink-faint); font-weight:400;}

  /* ---------- Board (kanban) ---------- */
  .board-toolbar{display:flex; align-items:center; gap:10px; margin-bottom:12px; flex-wrap:wrap;}
  .toggle-drop{
    font-size:12px; color:var(--ink-soft); background:var(--surface); border:1px solid var(--border);
    padding:6px 12px; border-radius:100px; cursor:pointer; display:flex; align-items:center; gap:7px;
  }
  .toggle-drop b{color:var(--ink);}
  .switch{width:28px; height:16px; border-radius:100px; background:var(--surface-3); position:relative; transition:background .15s;}
  .switch::after{content:""; position:absolute; top:2px; left:2px; width:12px; height:12px; border-radius:50%; background:var(--surface); transition:transform .15s; box-shadow:0 1px 2px rgba(0,0,0,.3);}
  .toggle-drop.on .switch{background:var(--accent);}
  .toggle-drop.on .switch::after{transform:translateX(12px);}

  .board{display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:12px; align-items:start;}
  .board-col{background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-m); padding:10px; min-height:60px;}
  .board-col.is-hideable{display:none;}
  .board-col.is-hideable.show{display:block;}
  .board-col-head{display:flex; align-items:center; justify-content:space-between; padding:2px 4px 10px; font-size:12px; font-weight:600;}
  .board-col-head .cnt{font-family:var(--font-mono); font-weight:500; color:var(--ink-faint);}
  .board-cards{display:flex; flex-direction:column; gap:8px; max-height:560px; overflow-y:auto; padding-right:2px;}
  .tcard{
    background:var(--surface); border:1px solid var(--border); border-left:3px solid var(--c); border-radius:var(--radius-s);
    padding:9px 10px; cursor:pointer; display:flex; flex-direction:column; gap:6px; box-shadow:var(--shadow);
  }
  .tcard:hover{border-color:var(--border-strong); border-left-color:var(--c);}
  .tcard .summary{font-size:12.5px; font-weight:500; line-height:1.4; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden;}
  .tcard .key{font-family:var(--font-mono); font-size:10.5px; color:var(--accent-strong);}
  .tcard .flow{font-size:10.5px; color:var(--ink-faint); display:flex; justify-content:space-between; gap:6px;}
  .empty-col{font-size:11.5px; color:var(--ink-faint); padding:10px 4px; text-align:center;}

  /* ---------- Lookup table ---------- */
  .lookup-bar{display:flex; gap:10px; margin-bottom:12px; flex-wrap:wrap; align-items:center;}
  .search-wrap{position:relative; flex:1; min-width:220px;}
  .search-wrap input{
    width:100%; padding:9px 12px 9px 32px; border-radius:100px; border:1px solid var(--border);
    background:var(--surface); color:var(--ink); font-family:var(--font-body); font-size:13px;
  }
  .search-wrap input:focus{border-color:var(--accent);}
  .search-wrap svg{position:absolute; left:11px; top:50%; transform:translateY(-50%); width:14px; height:14px; color:var(--ink-faint);}
  .filter-select{
    padding:8px 12px; border-radius:100px; border:1px solid var(--border); background:var(--surface); color:var(--ink);
    font-family:var(--font-body); font-size:12.5px;
  }
  .result-count{font-size:12px; color:var(--ink-faint); white-space:nowrap;}

  .org-filter{position:relative; display:inline-flex;}
  .org-filter-btn{display:inline-flex; align-items:center; gap:6px; cursor:pointer; font-family:inherit;}
  .org-filter-btn #orgFilterBtnLabel{white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:150px;}
  .org-filter-btn .caret{width:11px; height:11px; color:var(--ink-faint); transition:transform .15s; flex:none;}
  .org-filter.open .org-filter-btn{border-color:var(--accent);}
  .org-filter.open .org-filter-btn .caret{transform:rotate(180deg);}
  .org-filter-panel{
    position:absolute; top:calc(100% + 6px); left:0; z-index:20; min-width:230px; max-height:300px; overflow-y:auto;
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-m); box-shadow:var(--shadow);
    padding:6px; display:none; flex-direction:column; gap:1px;
  }
  .org-filter.open .org-filter-panel{display:flex;}
  .org-filter-option{
    display:flex; align-items:center; gap:8px; padding:7px 9px; border-radius:var(--radius-s); font-size:12.5px; cursor:pointer; color:var(--ink);
  }
  .org-filter-option:hover{background:var(--surface-2);}
  .org-filter-option input{accent-color:var(--accent); width:14px; height:14px; flex:none; margin:0;}
  .org-filter-actions{display:flex; justify-content:space-between; gap:8px; padding:7px 9px 2px; border-top:1px solid var(--border); margin-top:4px;}
  .org-filter-actions button{font-size:11px; color:var(--accent-strong); background:none; border:none; cursor:pointer; padding:0; text-decoration:underline; font-family:inherit;}

  .table-card{background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-l); box-shadow:var(--shadow); overflow:hidden;}
  /* 한 화면에 약 15행만 보이도록 높이를 고정하고, 그 이상은 이 영역 안에서만 스크롤한다
     (헤더 높이 35.5px + 행 높이 52px × 15). */
  .table-scroll{overflow-x:auto; overflow-y:auto; max-height:816px;}
  .table-scroll thead th{position:sticky; top:0; z-index:1;}
  table{width:100%; border-collapse:collapse; font-size:12.5px; min-width:820px;}
  thead th{
    text-align:left; padding:10px 14px; font-size:11px; font-weight:600; color:var(--ink-soft); text-transform:uppercase;
    letter-spacing:.04em; background:var(--surface-2); border-bottom:1px solid var(--border); cursor:pointer; white-space:nowrap; user-select:none;
  }
  thead th .arrow{opacity:.4; margin-left:3px; font-size:10px;}
  thead th.active .arrow{opacity:1; color:var(--accent-strong);}
  tbody td{padding:10px 14px; border-bottom:1px solid var(--border); vertical-align:top;}
  tbody tr{cursor:pointer; transition:background .1s;}
  tbody tr:hover{background:var(--surface-2);}
  tbody tr:last-child td{border-bottom:none;}
  td.summary-cell{max-width:360px;}
  td.summary-cell .k{font-family:var(--font-mono); font-size:10.5px; color:var(--accent-strong); display:block; margin-bottom:2px;}
  td.summary-cell .s{font-size:12.5px; font-weight:500; color:var(--ink); display:block;}

  .change-history-wrap{overflow-x:auto; overflow-y:auto; max-height:325px; border:1px solid var(--border); border-radius:var(--radius-l); box-shadow:var(--shadow); background:var(--surface);}
  .change-history-table{width:100%; border-collapse:collapse; table-layout:fixed; font-size:12.5px; min-width:720px;}
  .change-history-table thead th{cursor:default; position:sticky; top:0; background:var(--surface); z-index:1; box-shadow:0 1px 0 var(--border);}
  .change-history-table th:nth-child(1), .change-history-table td:nth-child(1){width:34%;}
  .change-history-table th:nth-child(2), .change-history-table td:nth-child(2){width:18%;}
  .change-history-table th:nth-child(3), .change-history-table td:nth-child(3){width:12%;}
  .change-history-table th:nth-child(4), .change-history-table td:nth-child(4){width:36%;}
  .ch-ticket .k{font-family:var(--font-mono); font-size:10.5px; color:var(--accent-strong); display:block; margin-bottom:2px;}
  .ch-ticket .s{font-size:12.5px; font-weight:500; color:var(--ink); display:block;}
  .ch-change{display:inline-flex; align-items:center; gap:6px; font-size:12.5px; color:var(--ink); flex-wrap:wrap;}
  .ch-change .arrow{color:var(--ink-faint);}
  .ch-change.na{color:var(--ink-faint); font-style:italic;}
  .ch-change.na svg{width:14px; height:14px; flex:none;}
  .ch-date{color:var(--ink-soft);}
  .change-history-table td.na{color:var(--ink-faint); font-style:italic;}
  td.flow-cell{font-size:12px; color:var(--ink-soft); white-space:nowrap;}
  .org-tag{
    display:inline-block; font-size:10px; color:var(--ink-faint); background:var(--surface-2);
    border-radius:5px; padding:1px 6px; margin-left:4px; vertical-align:middle;
  }
  td.date-cell{font-family:var(--font-mono); font-size:11.5px; color:var(--ink-soft); white-space:nowrap;}

  /* ---------- Drawer ---------- */
  .scrim{
    position:fixed; inset:0; background:rgba(8,14,12,.42); backdrop-filter:blur(1px);
    opacity:0; pointer-events:none; transition:opacity .18s ease; z-index:40;
  }
  .scrim.show{opacity:1; pointer-events:auto;}
  .drawer{
    position:fixed; top:0; right:0; height:100%; width:min(440px,92vw); background:var(--surface);
    border-left:1px solid var(--border); box-shadow:-16px 0 40px -20px rgba(0,0,0,.35);
    transform:translateX(100%); transition:transform .2s ease; z-index:41; overflow-y:auto;
  }
  .drawer.show{transform:translateX(0);}
  .drawer-head{padding:20px 22px 14px; border-bottom:1px solid var(--border); position:sticky; top:0; background:var(--surface); z-index:2;}
  .drawer-head .kind{font-size:11px; font-weight:600; letter-spacing:.07em; text-transform:uppercase; color:var(--accent-strong);}
  .drawer-close{
    position:absolute; top:16px; right:16px; width:28px; height:28px; border-radius:50%; border:1px solid var(--border);
    background:var(--surface-2); color:var(--ink-soft); cursor:pointer; font-size:14px; display:flex; align-items:center; justify-content:center;
  }
  .drawer-close:hover{background:var(--surface-3);}
  .drawer-title{font-size:16.5px; font-weight:700; margin:6px 34px 0 0; text-wrap:balance; line-height:1.4;}
  .drawer-body{padding:16px 22px 30px; display:flex; flex-direction:column; gap:18px;}
  .dl{display:grid; grid-template-columns:96px 1fr; gap:8px 12px; font-size:12.5px;}
  .dl dt{color:var(--ink-faint);}
  .dl dd{margin:0; color:var(--ink);}
  .dl dd.mono{font-family:var(--font-mono);}
  .field-block .k{font-size:11px; font-weight:600; letter-spacing:.05em; text-transform:uppercase; color:var(--ink-faint); margin-bottom:4px;}
  .field-block .v{font-size:13px; line-height:1.6;}
  .field-block .v.na{color:var(--ink-faint); font-style:italic;}
  .rel-ticket-list{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:2px;}
  .rel-ticket-list li{display:flex; align-items:baseline; gap:8px; padding:7px 10px; border-bottom:1px solid var(--border);}
  .rel-ticket-list li:last-child{border-bottom:none;}
  .rel-ticket-list .rt-key{font-family:var(--font-mono); font-size:11.5px; color:var(--accent-strong); font-weight:400; flex:0 0 auto; white-space:nowrap; text-decoration:none;}
  .rel-ticket-list a.rt-key:hover{text-decoration:underline;}
  .rel-ticket-list .rt-summary{font-size:12.5px; color:var(--ink); line-height:1.5;}

  /* ---------- Header outlink button ---------- */
  .btn-header-outlink{
    display:inline-flex; align-items:center; gap:6px; font-size:13px; font-weight:600; flex:none;
    color:var(--accent-contrast); background:var(--accent); border:1px solid var(--accent);
    padding:9px 14px; border-radius:100px; text-decoration:none; white-space:nowrap;
    transition:background .12s ease, transform .12s ease;
  }
  .btn-header-outlink:hover{background:var(--accent-strong); transform:translateY(-1px);}
  .btn-header-outlink svg{width:13px; height:13px; flex:none;}

  /* BR 작성 가이드라인 — 일감 접수하기와 같은 자리(헤더)에 두되, 실행 버튼이 아니라
     참고용 가이드임을 알 수 있도록 옅은 배경의 보조 버튼 형태로 구분한다. */
  .btn-header-guide{
    display:inline-flex; align-items:center; gap:6px; font-family:inherit; font-size:13px; font-weight:600; flex:none;
    color:var(--accent-strong); background:var(--accent-soft); border:1px solid var(--border-strong);
    padding:9px 14px; border-radius:100px; cursor:pointer; white-space:nowrap;
    transition:background .12s ease, border-color .12s ease;
  }
  .btn-header-guide:hover{background:var(--surface-3); border-color:var(--accent);}
  .btn-header-guide svg{width:13px; height:13px; flex:none;}

  /* ---------- Tabs ---------- */
  .tabs{
    display:inline-flex; gap:3px; margin-bottom:24px; padding:4px;
    background:var(--surface-2); border:1px solid var(--border); border-radius:100px;
  }
  .tab-btn{
    font-family:inherit; font-size:13.5px; font-weight:600; color:var(--ink-soft);
    background:none; border:none; border-radius:100px;
    padding:9px 20px; cursor:pointer; transition:background .14s ease, color .14s ease, box-shadow .14s ease;
  }
  .tab-btn:hover{color:var(--ink);}
  .tab-btn.active{background:var(--surface); color:var(--accent-strong); box-shadow:var(--shadow);}

  /* ---------- Placeholder / admin-managed info cards ---------- */
  .info-card{
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-l);
    box-shadow:var(--shadow); padding:16px 18px; font-size:13px; line-height:1.6;
  }
  .info-card.placeholder{
    display:flex; align-items:center; gap:9px;
    border-style:dashed; border-color:var(--border-strong); background:var(--surface-2);
    color:var(--ink-faint); box-shadow:none;
  }
  .info-card.placeholder svg{flex:none; width:16px; height:16px;}
  .info-card .outlink-row{display:flex; align-items:center; justify-content:space-between; gap:12px; flex-wrap:wrap;}
  .info-card .outlink-row a{display:inline-flex; align-items:center; gap:5px; font-weight:600; color:var(--accent-strong); text-decoration:none;}
  .info-card .outlink-row a:hover{text-decoration:underline;}

  /* ---------- BR guideline button + drawer content ---------- */
  .br-guide-btn{
    display:inline-flex; align-items:center; gap:8px; font-family:inherit; font-size:13.5px; font-weight:600;
    color:var(--accent-strong); background:var(--accent-soft); border:1px solid var(--accent);
    padding:11px 16px; border-radius:var(--radius-m); cursor:pointer; transition:background .12s ease, color .12s ease;
  }
  .br-guide-btn:hover{background:var(--accent); color:var(--accent-contrast);}
  .br-guide-btn svg{width:14px; height:14px; flex:none;}
  .br-guide-section{margin-bottom:16px;}
  .br-guide-section:last-child{margin-bottom:0;}
  .br-guide-section h4{margin:0 0 6px; font-size:12.5px; font-weight:700; color:var(--accent-strong);}
  .br-guide-section p{margin:0 0 6px; font-size:12.5px; line-height:1.7; color:var(--ink-soft);}
  .br-guide-section ul{margin:0; padding-left:18px; font-size:12.5px; line-height:1.7; color:var(--ink-soft);}
  .br-guide-section li{margin-bottom:3px;}
  .br-guide-section li b{color:var(--ink);}
  .br-guide-flow{display:flex; flex-wrap:wrap; align-items:center; gap:6px; font-size:11.5px; font-family:var(--font-mono);}
  .br-guide-flow .step{background:var(--surface-2); border:1px solid var(--border); border-radius:100px; padding:4px 10px; color:var(--ink);}
  .br-guide-flow .arrow{color:var(--ink-faint);}

  .issue-share-fab{
    position:fixed; right:22px; bottom:22px; z-index:35;
    display:flex; align-items:center;
    background:#E5484D; color:#FFFFFF;
    border-radius:100px; padding:8px;
    box-shadow:0 10px 28px -8px rgba(0,0,0,.38), 0 2px 8px rgba(0,0,0,.16);
    text-decoration:none; font-family:var(--font-body);
    overflow:hidden;
    transition:padding .22s ease, transform .15s ease, box-shadow .15s ease, background-color .15s ease;
  }
  .issue-share-fab:hover, .issue-share-fab:focus-visible{
    padding:8px 20px 8px 8px;
    transform:translateY(-2px) scale(1.02);
    box-shadow:0 16px 34px -8px rgba(0,0,0,.42), 0 4px 10px rgba(0,0,0,.2);
    background:#C93A3F;
  }
  .issue-share-fab .fab-icon{
    width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,.2);
    display:flex; align-items:center; justify-content:center; flex:0 0 auto;
  }
  .issue-share-fab .fab-icon svg{width:19px; height:19px;}
  .issue-share-fab .fab-label{
    display:flex; flex-direction:column; line-height:1.28;
    max-width:0; opacity:0; white-space:nowrap; overflow:hidden;
    transition:max-width .25s ease, opacity .18s ease, margin-left .25s ease;
  }
  .issue-share-fab:hover .fab-label, .issue-share-fab:focus-visible .fab-label{
    max-width:240px; opacity:1; margin-left:10px;
  }
  .issue-share-fab .fab-title{font-size:13.5px; font-weight:700; display:flex; align-items:center; gap:4px;}
  .issue-share-fab .fab-title svg{width:11px; height:11px; opacity:.85; flex:0 0 auto;}
  .issue-share-fab .fab-sub{font-size:10.5px; opacity:.88; font-weight:500;}

  .chatbot-fab{
    position:fixed; right:22px; bottom:86px; z-index:35;
    display:flex; align-items:center;
    background:var(--accent-strong); color:var(--accent-contrast);
    border:none; border-radius:100px; padding:8px; cursor:pointer;
    box-shadow:0 10px 28px -8px rgba(0,0,0,.38), 0 2px 8px rgba(0,0,0,.16);
    font-family:var(--font-body); overflow:hidden;
    transition:padding .22s ease, transform .15s ease, box-shadow .15s ease, background-color .15s ease;
  }
  .chatbot-fab:hover, .chatbot-fab:focus-visible{
    padding:8px 20px 8px 8px;
    transform:translateY(-2px) scale(1.02);
    box-shadow:0 16px 34px -8px rgba(0,0,0,.42), 0 4px 10px rgba(0,0,0,.2);
  }
  .chatbot-fab.is-open{background:var(--ink-soft);}
  .chatbot-fab .fab-icon{
    width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,.2);
    display:flex; align-items:center; justify-content:center; flex:0 0 auto;
  }
  .chatbot-fab .fab-icon svg{width:19px; height:19px;}
  .chatbot-fab .fab-label{
    display:flex; flex-direction:column; align-items:flex-start; line-height:1.28;
    max-width:0; opacity:0; white-space:nowrap; overflow:hidden;
    transition:max-width .25s ease, opacity .18s ease, margin-left .25s ease;
  }
  .chatbot-fab:hover .fab-label, .chatbot-fab:focus-visible .fab-label{
    max-width:220px; opacity:1; margin-left:10px;
  }
  .chatbot-fab .fab-title{font-size:13.5px; font-weight:700;}
  .chatbot-fab .fab-sub{font-size:10.5px; opacity:.88; font-weight:500;}

  .council-fab{
    position:fixed; right:22px; bottom:150px; z-index:35;
    display:flex; align-items:center;
    background:#0E7C86; color:#FFFFFF;
    border-radius:100px; padding:8px;
    box-shadow:0 10px 28px -8px rgba(0,0,0,.38), 0 2px 8px rgba(0,0,0,.16);
    text-decoration:none; font-family:var(--font-body);
    overflow:hidden;
    transition:padding .22s ease, transform .15s ease, box-shadow .15s ease, background-color .15s ease;
  }
  .council-fab:hover, .council-fab:focus-visible{
    padding:8px 20px 8px 8px;
    transform:translateY(-2px) scale(1.02);
    box-shadow:0 16px 34px -8px rgba(0,0,0,.42), 0 4px 10px rgba(0,0,0,.2);
    background:#0B646C;
  }
  .council-fab .fab-icon{
    width:36px; height:36px; border-radius:50%; background:rgba(255,255,255,.2);
    display:flex; align-items:center; justify-content:center; flex:0 0 auto;
  }
  .council-fab .fab-icon svg{width:19px; height:19px;}
  .council-fab .fab-label{
    display:flex; flex-direction:column; line-height:1.28;
    max-width:0; opacity:0; white-space:nowrap; overflow:hidden;
    transition:max-width .25s ease, opacity .18s ease, margin-left .25s ease;
  }
  .council-fab:hover .fab-label, .council-fab:focus-visible .fab-label{
    max-width:240px; opacity:1; margin-left:10px;
  }
  .council-fab .fab-title{font-size:13.5px; font-weight:700; display:flex; align-items:center; gap:4px;}
  .council-fab .fab-title svg{width:11px; height:11px; opacity:.85; flex:0 0 auto;}
  .council-fab .fab-sub{font-size:10.5px; opacity:.88; font-weight:500;}
  .council-fab[hidden]{display:none;}

  .chatbot-panel{
    position:fixed; right:22px; bottom:214px; z-index:40;
    width:360px; max-width:calc(100vw - 44px); height:min(500px, calc(100vh - 190px));
    background:var(--surface); border:1px solid var(--border); border-radius:var(--radius-l);
    box-shadow:0 20px 50px -12px rgba(0,0,0,.35), 0 6px 18px rgba(0,0,0,.18);
    display:flex; flex-direction:column; overflow:hidden;
  }
  .chatbot-panel[hidden]{display:none;}
  .chatbot-head{display:flex; align-items:flex-start; justify-content:space-between; gap:8px; padding:14px 14px 12px; border-bottom:1px solid var(--border); flex:none;}
  .chatbot-title{font-size:14px; font-weight:700; color:var(--ink);}
  .chatbot-sub{font-size:10.5px; color:var(--ink-faint); margin-top:3px; line-height:1.4;}
  .chatbot-close{background:none; border:none; padding:4px; color:var(--ink-faint); cursor:pointer; flex:none; border-radius:6px;}
  .chatbot-close:hover{color:var(--ink); background:var(--surface-2);}
  .chatbot-close svg{width:16px; height:16px; display:block;}
  .chatbot-messages{flex:1; min-height:0; overflow-y:auto; padding:14px; display:flex; flex-direction:column; gap:10px;}
  .cb-msg{display:flex;}
  .cb-msg.bot{justify-content:flex-start;}
  .cb-msg.user{justify-content:flex-end;}
  .cb-bubble{max-width:86%; padding:9px 12px; border-radius:var(--radius-m); font-size:12.5px; line-height:1.55;}
  .cb-msg.bot .cb-bubble{background:var(--surface-2); color:var(--ink); border-bottom-left-radius:4px;}
  .cb-msg.user .cb-bubble{background:var(--accent); color:var(--accent-contrast); border-bottom-right-radius:4px;}
  .cb-bubble b{font-weight:700;}
  .cb-bubble .cb-line{margin-top:4px;}
  .cb-bubble .cb-line:first-child{margin-top:0;}
  .cb-bubble .cb-list{margin-top:6px; display:flex; flex-direction:column; gap:5px;}
  .cb-bubble .cb-list-item{border-top:1px dashed var(--border); padding-top:5px;}
  .cb-bubble .cb-list-item:first-child{border-top:none; padding-top:0;}
  .cb-key-link{
    display:inline-flex; align-items:center; gap:4px; font-family:var(--font-mono); font-size:11px;
    color:var(--accent-strong); background:none; border:none; padding:0; cursor:pointer; text-decoration:underline; font-weight:600;
  }
  .cb-key-link:hover{color:var(--accent);}
  .chatbot-chips{display:flex; flex-wrap:wrap; gap:6px; padding:0 14px 10px; flex:none;}
  .chatbot-chip{
    font-size:11px; color:var(--accent-strong); background:var(--accent-soft); border:none;
    border-radius:100px; padding:5px 10px; cursor:pointer; font-family:inherit;
  }
  .chatbot-chip:hover{background:var(--accent); color:var(--accent-contrast);}
  .chatbot-form{display:flex; gap:8px; padding:10px 12px; border-top:1px solid var(--border); flex:none;}
  .chatbot-form input{
    flex:1; min-width:0; border:1px solid var(--border); border-radius:100px; padding:8px 14px;
    font-size:12.5px; font-family:inherit; background:var(--surface); color:var(--ink);
  }
  .chatbot-form input:focus{outline:none; border-color:var(--accent);}
  .chatbot-send{
    flex:none; width:34px; height:34px; border-radius:50%; border:none; background:var(--accent);
    color:var(--accent-contrast); display:flex; align-items:center; justify-content:center; cursor:pointer;
  }
  .chatbot-send:hover{background:var(--accent-strong);}
  .chatbot-send svg{width:15px; height:15px;}
  @media (max-width:480px){
    .chatbot-panel{right:12px; left:12px; width:auto; bottom:214px;}
    .chatbot-fab{right:12px;}
    .issue-share-fab{right:12px;}
    .council-fab{right:12px;}
  }
  .drawer-link{
    display:inline-flex; align-items:center; gap:6px; font-size:12.5px; font-weight:600; color:var(--accent-contrast);
    background:var(--accent); padding:8px 14px; border-radius:100px; text-decoration:none; width:fit-content;
  }
  .drawer-link:hover{background:var(--accent-strong);}
  hr.dv{border:none; border-top:1px solid var(--border); margin:0;}

  .history-section{display:flex; flex-direction:column; gap:12px;}
  .history-section-head{display:flex; align-items:center; justify-content:space-between;}
  .history-section-head h3{margin:0; font-size:13px; font-weight:700;}
  .history-section-head .cnt{font-size:11.5px; color:var(--ink-faint); font-weight:500;}
  .history-list{display:flex; flex-direction:column; gap:10px;}
  .history-item{background:var(--surface-2); border:1px solid var(--border); border-radius:var(--radius-m); padding:10px 12px; font-size:12.5px;}
  .history-item .h-head{display:flex; align-items:baseline; justify-content:space-between; gap:8px; margin-bottom:5px; flex-wrap:wrap;}
  .history-item .h-change{display:flex; align-items:center; gap:6px; font-weight:700; color:var(--ink); font-size:12.5px; flex:1 1 auto; min-width:0; word-break:keep-all;}
  .history-item .h-change svg{flex:none; width:14px; height:14px;}
  .history-item .h-change .arrow{color:var(--ink-faint); font-weight:400;}
  .history-item .h-time{font-size:10.5px; color:var(--ink-faint); font-family:var(--font-mono); white-space:nowrap;}
  .history-item .h-reason{color:var(--ink-soft); line-height:1.55;}
  .history-item .h-reason.na{color:var(--ink-faint); font-style:italic;}
  .history-item .h-meta{margin-top:6px; font-size:11px; color:var(--ink-faint); display:flex; flex-wrap:wrap; gap:10px;}
  .history-item.flagged .h-change{color:var(--st-review);}

  .data-note{
    font-size:12px; color:var(--ink-faint); background:var(--surface-2); border:1px solid var(--border);
    border-radius:var(--radius-m); padding:12px 16px; display:flex; gap:10px; align-items:flex-start;
  }
  .data-note svg{flex:none; margin-top:1px; width:15px; height:15px; color:var(--ink-faint);}

  footer{text-align:center; font-size:11.5px; color:var(--ink-faint); margin-top:36px;}

  @media (max-width:980px){
    .stats{grid-template-columns:repeat(3,1fr);}
  }
  @media (max-width:640px){
    .stats{grid-template-columns:repeat(2,1fr);}
    .app{padding:14px 12px 60px;}
  }
  @media (prefers-reduced-motion: reduce){
    *{transition:none !important; animation:none !important;}
  }

  /* ===== Refinement layer: display type, quiet hover states, small fixes ===== */
  .topbar h1, .section-head h2, .drawer-title{font-family:var(--font-display); font-weight:700;}
  .stat .n{font-family:var(--font-display); font-weight:600;}

  .stat{transition:border-color .15s ease, transform .15s ease;}
  .stat.clickable:hover{transform:translateY(-1px);}
  .release-card, .tcard{transition:border-color .15s ease;}
  .tcard:hover{transform:none;}

  .rg-coverage-fill{background:var(--accent);}
  .today-tag{color:#3A2600;}

  ::-webkit-scrollbar{width:10px; height:10px;}
  ::-webkit-scrollbar-track{background:transparent;}
  ::-webkit-scrollbar-thumb{background:var(--border-strong); border-radius:100px;}
  ::-webkit-scrollbar-thumb:hover{background:var(--ink-faint);}

</style>
</head>
<body>

<div class="app">

  <header class="topbar">
    <div>
      <h1><span class="brand-dot"></span>B tv 프로젝트 대시보드</h1>
      <div class="sub">이 페이지는 업로드 시점 스냅샷이며 <span class="sub-accent">실시간 연동은 아닙니다.</span> (기준일: <span class="sub-accent" id="headerUpdatedDate">2026-09-02</span>)</div>
    </div>
    <div class="header-actions">
      <a class="btn-header-outlink" href="https://jira.skbroadband.com/projects/BTVB/" target="_blank" rel="noopener noreferrer">
        일감 접수하기
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg>
      </a>
      <button type="button" class="btn-header-guide" id="brGuideBtn">
        BR 작성 가이드라인
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
      </button>
    </div>
  </header>

  <nav class="tabs" id="mainTabs">
    <button type="button" class="tab-btn active" data-tab="progress">프로젝트 진행 현황</button>
    <button type="button" class="tab-btn" data-tab="tickets">일감 관리</button>
  </nav>

  <div class="tab-panel" id="tab-progress">

    <div class="next-up-bar-slot" id="nextUpBarSlot"></div>

    <section class="section-divider">
      <div class="section-head">
        <div>
          <div class="eyebrow">Milestone Runway</div>
          <h2>마일스톤 타임라인</h2>
        </div>
        <div class="note">종료된 버전은 마일스톤 종료일 1개월 경과 시 미노출됩니다.</div>
      </div>
      <div class="runway-card">
        <div class="runway-legend" id="runwayLegend"></div>
        <div class="runway-body">
          <div class="runway-labels" id="runwayLabels"></div>
          <div class="runway-scroll">
            <div class="runway-inner" id="runwayInner"></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section-divider">
      <div class="section-head">
        <div>
          <div class="eyebrow">Release</div>
          <h2>버전 별 배포 현황</h2>
        </div>
        <a class="note-link" href="https://confluence.skbroadband.com/x/XeHHKg" target="_blank" rel="noopener noreferrer">배포 현황 상세<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="7" y1="17" x2="17" y2="7"/><polyline points="7 7 17 7 17 17"/></svg></a>
      </div>
      <div class="release-grid" id="releaseGrid"></div>
    </section>

  </div>

  <div class="tab-panel" id="tab-tickets" hidden>

    <section>
      <div class="section-head">
        <div>
          <div class="eyebrow">Overview</div>
          <h2>일감 현황 요약</h2>
        </div>
      </div>
      <div class="stats" id="stats"></div>
    </section>

    <section class="section-divider">
      <div class="section-head">
        <div>
          <div class="eyebrow">Change History</div>
          <h2>주요 변경사항</h2>
        </div>
        <div class="note">최근 변경 내역 순으로 20개만 보여집니다.</div>
      </div>
      <div class="change-history-wrap">
        <table class="change-history-table">
          <thead>
            <tr>
              <th>대상일감</th>
              <th>변경내용</th>
              <th>변경일</th>
              <th>메모</th>
            </tr>
          </thead>
          <tbody id="changeHistoryBody"></tbody>
        </table>
      </div>
    </section>

    <section class="section-divider">
      <div class="section-head">
        <div>
          <div class="eyebrow">Schedule</div>
          <h2>주요 일정</h2>
        </div>
      </div>
      <div id="nextScheduleCard"></div>
    </section>

    <section class="section-divider">
      <div class="section-head">
        <div>
          <div class="eyebrow">Issue Tracking</div>
          <h2>상태별 일감 보드</h2>
        </div>
        <div class="note">각 일감은 등록 순으로 보여집니다.</div>
      </div>
      <div class="board-toolbar">
        <div class="org-filter" id="boardOrgFilter">
          <button type="button" class="filter-select org-filter-btn" id="orgFilterBtn">
            <span id="orgFilterBtnLabel">조직: 전체</span>
            <svg class="caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
          <div class="org-filter-panel" id="orgFilterPanel"></div>
        </div>
        <button class="toggle-drop" id="dropToggle"><span class="switch"></span> Drop 일감 <b id="dropCount">0</b>건 표시</button>
        <button class="toggle-drop" id="receivedToggle"><span class="switch"></span> CR 이관 일감 <b id="receivedCount">0</b>건 표시</button>
      </div>
      <div class="board" id="board"></div>
    </section>

  </div>

</div>

<a class="issue-share-fab" href="https://confluence.skbroadband.com/x/2A5sKQ" target="_blank" rel="noopener noreferrer" title="프로젝트/일감 단위 이슈 공유 — Confluence 페이지 열기">
  <span class="fab-icon">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41L13.42 20.58a2 2 0 0 1-2.83 0L2.59 12.58V2H12.6l7.99 8a2 2 0 0 1 0 2.83z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>
  </span>
  <span class="fab-label">
    <span class="fab-title">이슈 공유
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
    </span>
    <span class="fab-sub">프로젝트/일감 단위 · Confluence 바로가기</span>
  </span>
</a>

<a class="council-fab" id="councilFab" href="#" target="_blank" rel="noopener noreferrer" title="지난 미디어 사업-기술 협의체 회의록 — Confluence 페이지 열기" hidden>
  <span class="fab-icon">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
  </span>
  <span class="fab-label">
    <span class="fab-title">미디어 사업-기술 협의체
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
    </span>
    <span class="fab-sub">지난 회의록 · Confluence 바로가기</span>
  </span>
</a>

<button type="button" class="chatbot-fab" id="chatbotFab" title="간단 문답봇 열기">
  <span class="fab-icon">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
  </span>
  <span class="fab-label">
    <span class="fab-title">간단 문답봇</span>
    <span class="fab-sub">일감·버전·일정 조회</span>
  </span>
</button>

<div class="chatbot-panel" id="chatbotPanel" hidden>
  <div class="chatbot-head">
    <div>
      <div class="chatbot-title">간단 문답봇</div>
      <div class="chatbot-sub">입력된 데이터를 규칙 기반으로 조회합니다. (AI 자유 응답 아님)</div>
    </div>
    <button type="button" class="chatbot-close" id="chatbotClose" aria-label="닫기">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>
  <div class="chatbot-messages" id="chatbotMessages"></div>
  <div class="chatbot-chips" id="chatbotChips"></div>
  <form class="chatbot-form" id="chatbotForm" novalidate>
    <input type="text" id="chatbotInput" placeholder="예: BTVB-3258 진행상황, 5.6.2 배포일정" maxlength="200" autocomplete="off">
    <button type="submit" class="chatbot-send" aria-label="전송">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
    </button>
  </form>
</div>

<div class="scrim" id="scrim"></div>
<aside class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer-head">
    <button class="drawer-close" id="drawerClose" aria-label="닫기">✕</button>
    <div class="kind" id="drawerKind">Ticket</div>
    <div class="drawer-title" id="drawerTitle"></div>
  </div>
  <div class="drawer-body" id="drawerBody"></div>
</aside>

<script>
const DATA = {"meta":{"masterUpdatedMax":"2026-09-03","releaseUpdatedMax":"2026-08-21","milestoneUpdatedMax":"2026-08-25","ticketCount":67,"releaseCount":7,"milestoneCount":77},"tickets":[{"key":"BTVB-3258","type":"BR","summary":"[RACE] import 형태 추천 시 콘텐츠 전시 누락 이슈","status":"사업 검토","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-26","updated":"2026-09-01","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3258"},{"key":"BTVB-3257","type":"BR","summary":"[RACE] 오늘 핫한 콘텐츠 RACE import(CCF/PVR)","status":"접수완료","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-25","updated":"2026-09-01","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3257"},{"key":"BTVB-3256","type":"BR","summary":"AI 커머스광고 채널 확대 대응 개발","status":"접수완료","reporter":"박지홍/커머스사업팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-25","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3256"},{"key":"BTVB-3255","type":"NF","summary":"AI 커머스광고 채널 확대 관련 검토 요청","status":"신규","reporter":"박지홍/커머스사업팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-24","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3255"},{"key":"BTVB-3254","type":"BR","summary":"(가칭)B tv+지상파 월정액 출시 검토","status":"신규","reporter":"백찬/Btv AX팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":"B tv, B tv pop, 모바일 B tv","poc":null,"created":"2026-08-19","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3254"},{"key":"BTVB-3253","type":"NF","summary":"CATV 소장형 VOD 이용 대상 가입자 상태 확인 기능 검토","status":"기술 검토","reporter":"김나윤/Btv AX팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-18","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3253"},{"key":"BTVB-3252","type":"BR","summary":"[RACE] 무료 GNB 메뉴 개편","status":"진행중","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-13","updated":"2026-09-03","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3252"},{"key":"BTVB-3251","type":"BR","summary":"[RACE] TV방송 GNB 메뉴 개편","status":"진행중","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-13","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3251"},{"key":"BTVB-3250","type":"BR","summary":"AI 쇼핑 서비스 Fade-out","status":"사업 검토","reporter":"권영은/커머스사업팀","assignee":"김진경/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-05","updated":"2026-08-13","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3250"},{"key":"BTVB-3249","type":"BR","summary":"[RACE] i2i-cbf 추천 결과 개선","status":"사업 검토","reporter":"허유진/Btv큐레이션팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":"RACE","poc":null,"created":"2026-08-04","updated":"2026-08-28","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3249"},{"key":"BTVB-3248","type":"BR","summary":"[RACE_B tv+] B tv+ 새로들어온 오류 확인 요청","status":"접수완료","reporter":"김현/Btv플러스팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-08-04","updated":"2026-08-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3248"},{"key":"BTVB-3247","type":"BR","summary":"[RACE] 다큐/라이프 GNB 메뉴 개편 - 메뉴 블록(2)","status":"접수완료","reporter":"허유진/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-30","updated":"2026-08-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3247"},{"key":"BTVB-3246","type":"BR","summary":"[RACE] 다큐/라이프 GNB 메뉴 개편 - 메뉴 블록(1)","status":"접수완료","reporter":"허유진/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-30","updated":"2026-08-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3246"},{"key":"BTVB-3245","type":"BR","summary":"[RACE_애니B tv+/max] 블록명 미 변경","status":"접수완료","reporter":"장정희/Btv플러스팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":"RACE","poc":null,"created":"2026-07-28","updated":"2026-08-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3245"},{"key":"BTVB-3244","type":"BR","summary":"[RACE] 다큐/라이프 GNB 메뉴 개편","status":"접수완료","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-27","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3244"},{"key":"BTVB-3243","type":"BR","summary":"[실시간] ㈜EPG 별도 수집 회차 연동 및 활용","status":"접수완료","reporter":"민경인/Btv AX팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-22","updated":"2026-08-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3243"},{"key":"BTVB-3242","type":"BR","summary":"넷플릭스 단독상품 관련 S-Market(CUG) 미 노출 추진","status":"접수완료","reporter":"임성진/미디어신규기획팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-20","updated":"2026-08-19","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3242"},{"key":"BTVB-3237","type":"BR","summary":"[성인] 새로 들어온 성인(19월정액only)","status":"접수완료","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-15","updated":"2026-08-19","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3237"},{"key":"BTVB-3235","type":"BR","summary":"모바일 B tv 리모컨 개선을 위한 STB 연계 기능 개발","status":"기술 검토","reporter":"이나현/모바일서비스기획팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":"CO, 모바일 B tv","poc":null,"created":"2026-07-09","updated":"2026-09-03","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3235"},{"key":"BTVB-3234","type":"BR","summary":"RACE 계정 신청 (guest)","status":"접수완료","reporter":"최요한/Web플랫폼개발팀","assignee":"허준식/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-09","updated":"2026-07-13","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3234"},{"key":"BTVB-3233","type":"BR","summary":"[RACE_B tv+] 애니메이션 분기별 race (26년 2분기)","status":"접수완료","reporter":"김현/Btv플러스팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-08","updated":"2026-07-08","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3233"},{"key":"BTVB-3232","type":"BR","summary":"[RACE] B tv 홈 신규 RACE 편성-Refresh","status":"접수완료","reporter":"한지윤/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-08","updated":"2026-07-23","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3232"},{"key":"BTVB-3230","type":"BR","summary":"[RACE] B tv 홈 신규 RACE 편성-import","status":"접수완료","reporter":"한지윤/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-08","updated":"2026-07-16","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3230"},{"key":"BTVB-3229","type":"BR","summary":"[RACE] B tv 홈 신규 RACE 편성","status":"접수완료","reporter":"한지윤/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-07","updated":"2026-07-16","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3229"},{"key":"BTVB-3227","type":"BR","summary":"B tv+ max 광고 노출 로직 개선 요청","status":"사업 검토","reporter":"이영은/Btv플러스팀","assignee":"정소연/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-03","updated":"2026-08-03","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3227"},{"key":"BTVB-3226","type":"BR","summary":"[프로필] 프로필 감지 및 전환 개선","status":"접수완료","reporter":"민경인/Btv AX팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":"CO","poc":null,"created":"2026-07-03","updated":"2026-08-03","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3226"},{"key":"BTVB-3225","type":"BR","summary":"[체감AI][에이닷] AI 홈 오퍼링 및 UI 일부 개선","status":"기술 검토","reporter":"장병채/Btv AI Agent기획팀","assignee":"장병채/Btv AI Agent기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-03","updated":"2026-09-03","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3225"},{"key":"BTVB-3224","type":"BR","summary":"[B tv+max] 하위버전 확대 제공을 위한 개발","status":"사업 검토","reporter":"백찬/Btv AX팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-03","updated":"2026-08-25","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3224"},{"key":"BTVB-3223","type":"BR","summary":"[RACE] 애니메이션 GNB 메뉴 개편 - 한일동시 메뉴","status":"접수완료","reporter":"강민지/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-07-02","updated":"2026-07-23","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3223"},{"key":"BTVB-3222","type":"BR","summary":"[RACE] 애니메이션 GNB 메뉴 개편 - 투니버스 메뉴","status":"접수완료","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-06-30","updated":"2026-07-30","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3222"},{"key":"BTVB-3221","type":"BR","summary":"[RACE] 애니메이션 GNB 메뉴 개편","status":"진행중","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-06-30","updated":"2026-08-06","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3221"},{"key":"BTVB-3220","type":"BR","summary":"block_preview_info (랭킹 블럭 안나오는 문제)","status":"접수완료","reporter":"최요한/Web플랫폼개발팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-06-25","updated":"2026-08-19","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3220"},{"key":"BTVB-3219","type":"BR","summary":"[RACE_max] B tv+ max 인기 급상승 명작 드라마, 인기 TOP Race 편성","status":"접수완료","reporter":"이영은/Btv플러스팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-06-24","updated":"2026-07-23","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3219"},{"key":"BTVB-3218","type":"BR","summary":"[모바일] 모바일 B tv 홈 메뉴 개편 - Import 및 로직 편성(장르별)","status":"접수완료","reporter":"권순환/Btv큐레이션팀","assignee":"최요한/Web플랫폼개발팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-06-23","updated":"2026-07-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3218"},{"key":"BTVB-3037","type":"BR","summary":"[매출][핫딜] 샵바이 - EUXP 섹션 상태 갱신 요청","status":"접수완료","reporter":"김혜선/홈쇼핑사업팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":"CO","poc":null,"created":"2026-01-06","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3037"},{"key":"BTVB-3126","type":"BR","summary":"[설정] STB 설정값 현행 적재 요청","status":"보류(DROP)","reporter":"이민정/Btv AX팀","assignee":"이민정/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-10","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3126"},{"key":"BTVB-3014","type":"BR","summary":"[설정] '자녀 안심 설정' 시 콘텐츠 단위 포스터 노출 제어 고도화","status":"보류(DROP)","reporter":"허유진/Btv큐레이션팀","assignee":"김나윤/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2025-11-13","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3014"},{"key":"BTVB-3041","type":"BR","summary":"전체 화면 가격 표기 부가세 포함가로 통일","status":"보류(DROP)","reporter":"김주난/Btv AX팀","assignee":"김주난/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-09","updated":"2026-07-23","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3041"},{"key":"BTVB-3158","type":"BR","summary":"SK Pay 명칭 변경 및 결제 플로우 개선 검토","status":"HOLD","reporter":"김주난/Btv AX팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-04-14","updated":"2026-09-02","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3158"},{"key":"BTVB-3069","type":"BR","summary":"[시놉시스/재생화면] 시놉 일원화 및 바로 재생 정책 개선","status":"접수완료","reporter":"김주난/Btv AX팀","assignee":"김주난/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-21","updated":"2026-09-01","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3069"},{"key":"BTVB-3100","type":"BR","summary":"[B tv_EW] 쇼츠(Shorts) 콘텐츠 전용 UI 신규 개발","status":"보류(DROP)","reporter":"김상수/VoD사업팀","assignee":"정소연/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-04","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3100"},{"key":"BTVB-3044","type":"BR","summary":"[FAST] 정주행TV 서비스 기능 고도화","status":"보류(DROP)","reporter":"김상수/VoD사업팀","assignee":"정소연/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-15","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3044"},{"key":"BTVB-3038","type":"BR","summary":"[광고] STB 부팅 On (웜/콜드) 광고 서비스 개발","status":"보류(DROP)","reporter":"제환종/IPTV 3.0 BM TF","assignee":"정소연/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-06","updated":"2026-07-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3038"},{"key":"BTVB-3034","type":"BR","summary":"[광고] 홈 아웃 광고 기능 개발","status":"보류(DROP)","reporter":"양정우/광고기술팀","assignee":"정소연/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2025-12-23","updated":"2026-08-31","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3034"},{"key":"BTVB-3066","type":"BR","summary":"[매출][홈쇼핑모아보기] 진입 화면 개편","status":"보류(DROP)","reporter":"임지환/홈쇼핑사업팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-19","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3066"},{"key":"BTVB-3067","type":"BR","summary":"[매출][핫딜] 타임딜(시간 한정 특가) 운영 위한 고도화","status":"보류(DROP)","reporter":"김혜선/홈쇼핑사업팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-19","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3067"},{"key":"BTVB-3068","type":"BR","summary":"[매출][핫딜][홈쇼핑모아보기] 로딩 시간 단축 및 진입 시나리오 개선","status":"보류(DROP)","reporter":"박예니/홈쇼핑사업팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-19","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3068"},{"key":"BTVB-3050","type":"BR","summary":"[AI_BM][AI 커머스광고] PPL 데이터 수집 및 연동기능 구현","status":"보류(DROP)","reporter":"박지홍/커머스사업팀","assignee":"김진경/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-15","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3050"},{"key":"BTVB-3051","type":"BR","summary":"[AI_BM][AI 커머스광고] 프로그램 단위 서비스 적용","status":"보류(DROP)","reporter":"박지홍/커머스사업팀","assignee":"김진경/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-15","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3051"},{"key":"BTVB-3053","type":"BR","summary":"[AI_BM][AI커머스광고]서비스 기능 개선 (분석/전송/결과표시","status":"drop","reporter":null,"assignee":null,"reqVersion":"B tv VCS 5.6.2","component":null,"poc":"B tv","created":null,"updated":null,"jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3053"},{"key":"BTVB-3054","type":"BR","summary":"[딥메타]콘텐츠 썸네일 이미지 추출 자동화 개발","status":"보류(DROP)","reporter":"임예은/Btv큐레이션팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-15","updated":"2026-07-24","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3054"},{"key":"BTVB-3045","type":"BR","summary":"[AD slot] 실시간 채널 마케팅 인벤토리 기능 고도화","status":"보류(DROP)","reporter":"정재훈/Btv큐레이션팀","assignee":"정소연/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-15","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3045"},{"key":"BTVB-3104","type":"BR","summary":"[PI][EUXP] 라이브러리 복사 기능 개발 요청(B tv+프리미엄→B tv+)","status":"보류(DROP)","reporter":"이영은/Btv플러스팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-04","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3104"},{"key":"BTVB-3024","type":"BR","summary":"[스마트알림] 자동 발송되는 시스템 알림 내 마케팅 문구 추가 노출","status":"보류(DROP)","reporter":"임성빈/PPC사업팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2025-12-08","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3024"},{"key":"BTVB-3063","type":"BR","summary":"[VOD] 음성 언어 통합 상품 및 다중 음성 서비스 제공","status":"보류(DROP)","reporter":"임성빈/PPC사업팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-19","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3063"},{"key":"BTVB-3062","type":"BR","summary":"[실시간] 캐치온 채널 미니EPG 내 '처음부터 보기' 서비스 제공","status":"보류(DROP)","reporter":"김세빈/월정액리텐션팀","assignee":"김나윤/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-19","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3062"},{"key":"BTVB-3102","type":"BR","summary":"[ZEM/검색] 키즈 앱 딥링크 편성 개발 요청","status":"보류(DROP)","reporter":"현연주/Btv서비스기획팀","assignee":"이설화/Btv서비스기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-04","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3102"},{"key":"BTVB-3073","type":"BR","summary":"[체감AI][실시간] DCA 내 추천 채널 제공","status":"보류(DROP)","reporter":"김진경/Btv AX팀","assignee":"김진경/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-01-29","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3073"},{"key":"BTVB-3112","type":"BR","summary":"[체감AI][AI Tip] 알림형 AI Tip 고도화","status":"보류(DROP)","reporter":"김나윤/Btv AX팀","assignee":"김나윤/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-05","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3112"},{"key":"BTVB-3116","type":"BR","summary":"[체감AI][AI Tip] 제안 접점 확대 및 기타 개선","status":"보류(DROP)","reporter":"민경인/Btv AX팀","assignee":"민경인/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":"CO","poc":null,"created":"2026-02-09","updated":"2026-04-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3116"},{"key":"BTVB-3143","type":"BR","summary":"[홈] GNB 메뉴 개편 및 Today B tv 고도화 개발","status":"보류(DROP)","reporter":"백찬/Btv AX팀","assignee":"백찬/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-03-05","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3143"},{"key":"BTVB-3080","type":"BR","summary":"[체감AI][에이닷] 미디어 에이전트 검색 결과 고도화","status":"보류(DROP)","reporter":"권성한/Btv AI Agent기획팀","assignee":"권성한/Btv AI Agent기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-03","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3080"},{"key":"BTVB-3092","type":"BR","summary":"[체감AI][에이닷] 서비스 에이전트 고도화","status":"보류(DROP)","reporter":"이주연/Btv AI Agent기획팀","assignee":"이주연/Btv AI Agent기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-03","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3092"},{"key":"BTVB-3086","type":"BR","summary":"[체감AI][에이닷] 실시간 채널 대화 개선","status":"보류(DROP)","reporter":"이주연/Btv AI Agent기획팀","assignee":"이주연/Btv AI Agent기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-03","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3086"},{"key":"BTVB-3090","type":"BR","summary":"[체감AI][에이닷] 에이닷 서비스 운영 고도화","status":"보류(DROP)","reporter":"박현진/Btv AI Agent기획팀","assignee":"박현진/Btv AI Agent기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-03","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3090"},{"key":"BTVB-3099","type":"BR","summary":"[AI_BM][에이닷] 커머스 가상채널 발화 이동 지원","status":"진행중","reporter":"권성한/Btv AI Agent기획팀","assignee":"장병채/Btv AI Agent기획팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-02-04","updated":"2026-07-21","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3099"},{"key":"BTVB-3144","type":"BR","summary":"[재생][인사이드] 인물정보 포커스기반 경량화 및 맥락요약 추가","status":"보류(DROP)","reporter":"김주난/Btv AX팀","assignee":"김주난/Btv AX팀","reqVersion":"B tv VCS 5.6.2","component":null,"poc":null,"created":"2026-03-05","updated":"2026-08-20","jiraUrl":"https://jira.skbroadband.com/browse/BTVB-3144"}],"releases":[{"version":"5.6.2","group":"1그룹","dueDate":"2026-11-24","platform":"B tv","devices":"Smart3, AI5","summary":null,"ticketCount":30,"status":"배포예정","issues":null,"changes":null,"decisions":null,"updated":"2026-08-21","dataStatus":"정상","deployedUnits":null,"totalUnits":null,"coveragePct":null,"coverageBasis":null},{"version":"5.6.2","group":"2그룹","dueDate":"2026-12-09","platform":"B tv","devices":"AI4 vision, AI2, Smart3 mini","summary":null,"ticketCount":30,"status":"배포예정","issues":null,"changes":null,"decisions":null,"updated":"2026-08-21","dataStatus":"정상","deployedUnits":null,"totalUnits":null,"coveragePct":null,"coverageBasis":null},{"version":"5.6.2","group":"3그룹","dueDate":"2027-01-20","platform":"B tv","devices":"AI Soundmax","summary":null,"ticketCount":30,"status":"배포예정","issues":null,"changes":null,"decisions":null,"updated":"2026-08-21","dataStatus":"정상","deployedUnits":null,"totalUnits":null,"coveragePct":null,"coverageBasis":null},{"version":"5.6.1 #1","group":"1그룹","dueDate":"2026-03-10","platform":"B tv","devices":"AI2, AI5","summary":null,"ticketCount":20,"status":"배포완료","issues":null,"changes":null,"decisions":null,"updated":"2026-08-20","dataStatus":"정상","deployedUnits":14510,"totalUnits":433924,"coveragePct":3.3,"coverageBasis":"5.6.1"},{"version":"5.6.1 #2","group":"1그룹","dueDate":"2026-06-22","platform":"B tv","devices":"Smart3, AI5","summary":"B tv+ max 상품 출시","ticketCount":7,"status":"상시배포","issues":null,"changes":null,"decisions":null,"updated":null,"dataStatus":"정상","deployedUnits":3777459,"totalUnits":4372467,"coveragePct":86.4,"coverageBasis":"5.6.1 #2"},{"version":"5.6.1 #2","group":"2그룹","dueDate":"2026-07-28","platform":"B tv","devices":"AI2, Smart3 mini, AI 4 vision","summary":"B tv+ max 상품 출시","ticketCount":7,"status":"상시배포","issues":null,"changes":null,"decisions":null,"updated":null,"dataStatus":"정상","deployedUnits":612966,"totalUnits":683641,"coveragePct":89.7,"coverageBasis":"5.6.1 #2"},{"version":"5.6.1 #2","group":"3그룹","dueDate":"2026-09-08","platform":"B tv","devices":"AI Soundmax","summary":"B tv+ max 상품 출시","ticketCount":7,"status":"배포예정","issues":null,"changes":null,"decisions":null,"updated":null,"dataStatus":"정상","deployedUnits":5,"totalUnits":32305,"coveragePct":0.0,"coverageBasis":"5.6.1 #2"}],"milestones":[{"version":"5.6.2","name":"고객자문단 결과 공유/반영 범위 확정","start":"2026-09-14","finish":{"raw":"2026-09-31","invalid":true},"status":null,"updated":"2026-08-25","dataStatus":null},{"version":"5.6.2","name":"고객자문단 조사","start":"2026-08-31","finish":"2026-09-11","status":null,"updated":"2026-08-25","dataStatus":"정상"},{"version":"5.6.2","name":"계약","start":"2026-07-07","finish":"2026-07-13","status":null,"updated":"2026-07-14","dataStatus":"정상"},{"version":"5.6.1 #2","name":"UI 검수 후 수정 개발","start":"2026-05-06","finish":"2026-05-08","status":null,"updated":"2026-05-11","dataStatus":"정상"},{"version":"5.6.2","name":"BR 사전 리뷰","start":"2026-02-24","finish":"2026-02-24","status":null,"updated":"2026-03-17","dataStatus":"정상"},{"version":"5.6.2","name":"BR Fix","start":"2026-03-11","finish":"2026-03-31","status":null,"updated":"2026-04-06","dataStatus":"정상"},{"version":"5.6.1","name":"Secure coding test_2차","start":"2026-03-06","finish":"2026-03-06","status":null,"updated":"2026-03-10","dataStatus":"정상"},{"version":"5.6.2","name":"Secure Coding test_1차","start":"2026-10-15","finish":"2026-10-15","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.1 #2","name":"Pre-PRD 편성","start":"2026-04-20","finish":"2026-04-21","status":null,"updated":"2026-04-23","dataStatus":"정상"},{"version":"5.6.1 #2","name":"3차 그룹 Release","start":"2026-09-08","finish":"2026-09-08","status":null,"updated":"2026-04-09","dataStatus":"정상"},{"version":"5.6.1 #2","name":"3차 그룹 QA","start":"2026-08-03","finish":"2026-09-07","status":null,"updated":"2026-04-09","dataStatus":"정상"},{"version":"5.6.1 #2","name":"개발","start":"2026-03-25","finish":"2026-04-17","status":null,"updated":"2026-04-20","dataStatus":"정상"},{"version":"5.6.1 #2","name":"견적 취합","start":"2026-01-22","finish":"2026-01-27","status":null,"updated":"2026-01-28","dataStatus":"정상"},{"version":"5.6.1 #2","name":"2차 그룹 Release","start":"2026-07-28","finish":"2026-07-28","status":null,"updated":"2026-07-28","dataStatus":"정상"},{"version":"5.6.1 #2","name":"2차 그룹 QA","start":"2026-06-22","finish":"2026-07-24","status":null,"updated":"2026-07-28","dataStatus":"정상"},{"version":"5.6.1 #2","name":"1차 그룹 Release","start":"2026-06-22","finish":"2026-06-22","status":null,"updated":"2026-06-23","dataStatus":"정상"},{"version":"5.6.1 #2","name":"구글 인증","start":"2026-06-10","finish":"2026-06-16","status":null,"updated":"2026-06-17","dataStatus":"정상"},{"version":"5.6.1 #2","name":"1차 그룹 QA","start":"2026-05-11","finish":"2026-06-18","status":null,"updated":"2026-06-22","dataStatus":"정상"},{"version":"5.6.1 #2","name":"VCS CCU 부하 test2","start":"2026-06-17","finish":"2026-06-30","status":null,"updated":"2026-07-23","dataStatus":"정상"},{"version":"5.6.1 #2","name":"H/E PRD 배포","start":"2026-06-08","finish":"2026-06-11","status":null,"updated":"2026-06-12","dataStatus":"정상"},{"version":"5.6.1 #2","name":"Secure coding test_2차","start":"2026-06-11","finish":"2026-06-19","status":null,"updated":"2026-06-30","dataStatus":"정상"},{"version":"5.6.1 #2","name":"VCS CCU 부하 test1","start":"2026-05-07","finish":"2026-05-15","status":null,"updated":"2026-05-18","dataStatus":"정상"},{"version":"5.6.1 #2","name":"UI 검수","start":"2026-04-27","finish":"2026-05-06","status":null,"updated":"2026-05-07","dataStatus":"정상"},{"version":"5.6.1 #2","name":"F/W 빌드","start":"2026-04-24","finish":"2026-04-27","status":null,"updated":"2026-04-28","dataStatus":"정상"},{"version":"5.6.1 #2","name":"Pre-PRD 배포","start":"2026-04-20","finish":"2026-04-21","status":null,"updated":"2026-04-22","dataStatus":"정상"},{"version":"5.6.1 #2","name":"Native/WEB- H/E 정합","start":"2026-04-20","finish":"2026-04-24","status":null,"updated":"2026-04-28","dataStatus":"정상"},{"version":"5.6.1 #2","name":"GUI 디자인","start":"2026-01-29","finish":"2026-02-03","status":null,"updated":"2026-02-04","dataStatus":"정상"},{"version":"5.6.1 #2","name":"Secure coding test_1차","start":"2026-04-27","finish":"2026-04-30","status":null,"updated":"2026-05-11","dataStatus":"정상"},{"version":"5.6.1 #2","name":"UI 시나리오 작성","start":"2026-01-22","finish":"2026-01-29","status":null,"updated":"2026-02-04","dataStatus":"정상"},{"version":"5.6.2","name":"2차 그룹 Google 인증","start":"2026-12-29","finish":"2026-12-31","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"1차 그룹 Google 인증","start":"2026-11-18","finish":"2026-11-23","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"stg 편성","start":"2026-09-14","finish":"2026-09-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"pre-PRD 편성","start":"2026-09-30","finish":"2026-10-02","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"H/E PRD 배포","start":"2026-11-09","finish":"2026-11-17","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"H/E Pre-PRD 배포","start":"2026-09-28","finish":"2026-10-02","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"개발 정합(native/Web/MW)","start":"2026-09-21","finish":"2026-10-02","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"3차 그룹 Release","start":"2027-02-15","finish":"2027-02-15","status":null,"updated":"2026-07-28","dataStatus":"정상"},{"version":"5.6.2","name":"3차 그룹 QA","start":"2027-01-11","finish":"2027-02-12","status":null,"updated":"2026-07-28","dataStatus":"정상"},{"version":"5.6.2","name":"2차 그룹 Release","start":"2027-01-05","finish":"2027-01-05","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"1차 그룹 Release","start":"2026-11-24","finish":"2026-11-24","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"Secure coding test_2차","start":"2026-11-18","finish":"2026-11-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"2차 그룹 QA","start":"2026-11-30","finish":"2027-01-01","status":null,"updated":"2026-07-28","dataStatus":"정상"},{"version":"5.6.2","name":"1차 그룹 QA","start":"2026-10-19","finish":"2026-11-20","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"VCS CCU 부하 test_2차","start":"2026-11-18","finish":"2026-11-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"VCS CCU 부하 test_1차","start":"2026-10-15","finish":"2026-10-15","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"UI 검수 수정","start":"2026-10-12","finish":"2026-10-16","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"UI 검수","start":"2026-10-06","finish":"2026-10-08","status":null,"updated":"2026-07-08","dataStatus":"정상"},{"version":"5.6.2","name":"Native 개발","start":"2026-07-13","finish":"2026-09-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"H/E 개발","start":"2026-07-13","finish":"2026-09-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"M/W, 제조사 개발","start":"2026-07-13","finish":"2026-09-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"Web 개발","start":"2026-07-06","finish":"2026-09-18","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"예산 협의/일감 확정/품의","start":"2026-06-08","finish":"2026-07-07","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"견적 취합","start":"2026-05-26","finish":"2026-06-30","status":null,"updated":"2026-06-04","dataStatus":"정상"},{"version":"5.6.2","name":"GUI 디자인","start":"2026-04-20","finish":"2026-07-03","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"UI 시나리오 작성","start":"2026-04-20","finish":"2026-07-03","status":null,"updated":"2026-07-07","dataStatus":"정상"},{"version":"5.6.2","name":"Spec fix","start":"2026-05-22","finish":"2026-05-29","status":null,"updated":"2026-06-04","dataStatus":"정상"},{"version":"5.6.2","name":"CR/IM 리뷰","start":"2026-05-15","finish":"2026-05-21","status":null,"updated":"2026-05-26","dataStatus":"정상"},{"version":"5.6.2","name":"CR 전환","start":"2026-03-30","finish":"2026-04-17","status":null,"updated":"2026-04-21","dataStatus":"정상"},{"version":"5.6.2","name":"BR 리뷰","start":"2026-03-04","finish":"2026-03-10","status":null,"updated":"2026-03-26","dataStatus":"정상"},{"version":"5.6.1","name":"Secure coding test_1차","start":"2026-02-23","finish":"2026-02-24","status":null,"updated":"2026-02-24","dataStatus":"정상"},{"version":"5.6.1","name":"CLONE - UI 검수 수정","start":"2026-01-26","finish":"2026-01-30","status":null,"updated":"2025-12-23","dataStatus":"정상"},{"version":"5.6.1","name":"CLONE - 2차 그룹 Release","start":"2026-04-07","finish":"2026-04-07","status":null,"updated":"2025-12-23","dataStatus":"정상"},{"version":"5.6.1","name":"CLONE - 2차 그룹 QA","start":"2026-03-09","finish":"2026-04-06","status":null,"updated":"2025-12-23","dataStatus":"정상"},{"version":"5.6.1","name":"CLONE - CTS 인증","start":"2026-03-04","finish":"2026-03-09","status":null,"updated":"2025-12-23","dataStatus":"정상"},{"version":"5.6.1","name":"CLONE - VCS CCU 부하 test2","start":"2026-03-03","finish":"2026-03-03","status":null,"updated":"2025-12-23","dataStatus":"정상"},{"version":"5.6.1","name":"H/E Pre-PRD 배포&편성","start":"2026-01-12","finish":"2026-01-16","status":null,"updated":"2025-12-30","dataStatus":"정상"},{"version":"5.6.1","name":"H/E PRD 배포","start":"2026-02-23","finish":"2026-02-27","status":null,"updated":"2025-12-30","dataStatus":"정상"},{"version":"5.6.1","name":"1차 그룹 Release","start":"2026-03-10","finish":"2026-03-10","status":null,"updated":"2025-12-30","dataStatus":"정상"},{"version":"5.6.1","name":"1차 그룹 QA","start":"2026-02-02","finish":"2026-03-09","status":null,"updated":"2025-12-30","dataStatus":"정상"},{"version":"5.6.1","name":"CTS 인증","start":"2026-03-05","finish":"2026-03-09","status":null,"updated":"2026-03-10","dataStatus":"정상"},{"version":"5.6.1","name":"VCS CCU 부하 test2","start":"2026-03-05","finish":"2026-03-06","status":null,"updated":"2026-03-30","dataStatus":"정상"},{"version":"5.6.1","name":"VCS CCU 부하 test1","start":"2026-01-30","finish":"2026-02-03","status":null,"updated":"2026-08-20","dataStatus":"정상"},{"version":"5.6.1","name":"H/E Pre-PRD 배포&편성(에이닷)","start":"2026-01-12","finish":"2026-01-16","status":null,"updated":"2026-01-29","dataStatus":"정상"},{"version":"5.6.1","name":"H/E PRD 배포","start":"2026-02-26","finish":"2026-03-04","status":null,"updated":"2026-03-10","dataStatus":"정상"},{"version":"5.6.1","name":"1차 그룹 Release","start":"2026-03-10","finish":"2026-03-10","status":null,"updated":"2026-03-10","dataStatus":"정상"},{"version":"5.6.1","name":"1차 그룹 QA","start":"2026-02-02","finish":"2026-03-09","status":null,"updated":"2026-03-10","dataStatus":"정상"},{"version":"5.6.1","name":"UI 검수_1차(Voice ID, 에이닷)","start":"2026-01-23","finish":"2026-01-30","status":null,"updated":"2026-02-05","dataStatus":"정상"}]};

DATA.history = [{"id":"H-001","ticketKey":"BTVB-3100","summary":"[B tv_EW] 쇼츠(Shorts) 콘텐츠 전용 UI 신규 개발","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"필요성 공감하나 시의성 높지 않아 당해년도 추진 우선순위는 검토 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-002","ticketKey":"BTVB-3044","summary":"[FAST] 정주행TV 서비스 기능 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"필요성 공감하나 시의성 높지 않아 당해년도 추진 우선순위는 검토 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-003","ticketKey":"BTVB-3038","summary":"[광고] STB 부팅 On (웜/콜드) 광고 서비스 개발","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"필요성 공감하나 시의성 높지 않아 당해년도 추진 우선순위는 검토 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-004","ticketKey":"BTVB-3034","summary":"[광고] 홈 아웃 광고 기능 개발","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"필요성 공감하나 시의성 높지 않아 당해년도 추진 우선순위는 검토 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-005","ticketKey":"BTVB-3037","summary":"[매출][핫딜] 샵바이 - EUXP 섹션 상태 갱신 요청","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"필요성 공감하나 시의성 높지 않아 당해년도 추진 우선순위는 검토 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-006","ticketKey":"BTVB-3066","summary":"[매출][홈쇼핑모아보기] 진입 화면 개편","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"기술검토 결과 별도 투자 필요하여 보류","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-007","ticketKey":"BTVB-3067","summary":"[매출][핫딜] 타임딜(시간 한정 특가) 운영 위한 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"투입 리소스 기반하여 의사결정 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-008","ticketKey":"BTVB-3068","summary":"[매출][핫딜][홈쇼핑모아보기] 로딩 시간 단축 및 진입 시나리","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"투입 리소스 기반하여 의사결정 필요","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-009","ticketKey":"BTVB-3050","summary":"[AI_BM][AI 커머스광고] PPL 데이터 수집 및 연동기능 구현","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"MVP 버전 성과에 기반해 정식 서비스 컨센서스가 필요함","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-010","ticketKey":"BTVB-3051","summary":"[AI_BM][AI 커머스광고] 프로그램 단위 서비스 적용","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"MVP 버전 성과에 기반해 정식 서비스 컨센서스가 필요함","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-011","ticketKey":"BTVB-3053","summary":"[AI_BM][AI커머스광고]서비스 기능 개선 (분석/전송/결과표시","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":"MVP 버전 성과에 기반해 정식 서비스 컨센서스가 필요함","impact":null,"deciders":"본부 내 의사결정","changedAt":"2026-03-06","evidenceUrl":"https://confluence.skbroadband.com/x/8qVtKg","registrant":"PMO","dataStatus":"정상"},{"id":"H-012","ticketKey":"BTVB-3041","summary":"전체 화면 가격 표기 부가세 포함가로 통일","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-013","ticketKey":"BTVB-3014","summary":"[설정] '자녀 안심 설정' 시 콘텐츠 단위 포스터 노출 제어 고","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-014","ticketKey":"BTVB-3054","summary":"[딥메타]콘텐츠 썸네일 이미지 추출 자동화 개발","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-015","ticketKey":"BTVB-3045","summary":"[AD slot] 실시간 채널 마케팅 인벤토리 기능 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-016","ticketKey":"BTVB-3104","summary":"[PI][EUXP] 라이브러리 복사 기능 개발 요청(B tv+프리미엄→B","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-017","ticketKey":"BTVB-3024","summary":"[스마트알림] 자동 발송되는 시스템 알림 내 마케팅 문구 추가","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-018","ticketKey":"BTVB-3063","summary":"[VOD] 음성 언어 통합 상품 및 다중 음성 서비스 제공","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-019","ticketKey":"BTVB-3062","summary":"[실시간] 캐치온 채널 미니EPG 내 '처음부터 보기' 서비스 제공","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-020","ticketKey":"BTVB-3102","summary":"[ZEM/검색] 키즈 앱 딥링크 편성 개발 요청","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-021","ticketKey":"BTVB-3073","summary":"[체감AI][실시간] DCA 내 추천 채널 제공","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-022","ticketKey":"BTVB-3112","summary":"[체감AI][AI Tip] 알림형 AI Tip 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-023","ticketKey":"BTVB-3116","summary":"[체감AI][AI Tip] 제안 접점 확대 및 기타 개선","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-024","ticketKey":"BTVB-3143","summary":"[홈] GNB 메뉴 개편 및 Today B tv 고도화 개발","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-025","ticketKey":"BTVB-3069","summary":"[시놉시스/재생화면] 시놉 일원화 및 바로 재생 정책 개선","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-026","ticketKey":"BTVB-3080","summary":"[체감AI][에이닷] 미디어 에이전트 검색 결과 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-027","ticketKey":"BTVB-3092","summary":"[체감AI][에이닷] 서비스 에이전트 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-028","ticketKey":"BTVB-3086","summary":"[체감AI][에이닷] 실시간 채널 대화 개선","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-029","ticketKey":"BTVB-3090","summary":"[체감AI][에이닷] 에이닷 서비스 운영 고도화","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-030","ticketKey":"BTVB-3099","summary":"[AI_BM][에이닷] 커머스 가상채널 발화 이동 지원","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-031","ticketKey":"BTVB-3144","summary":"[재생][인사이드] 인물정보 포커스기반 경량화 및 맥락요약 추가","flagged":false,"changeField":"Status","before":"접수","after":"drop","reason":null,"impact":null,"deciders":null,"changedAt":"2026-03-06","evidenceUrl":null,"registrant":"PMO","dataStatus":"정상"},{"id":"H-032","ticketKey":"BTVB-3037","summary":"[매출][핫딜] 샵바이EUXP 섹션 상태 갱신 요청","flagged":true,"dataStatus":"확인필요: 변경항목, 변경일","changedAt":null},{"id":"H-033","ticketKey":"BTVB-3126","summary":"[설정] STB 설정값 현행 적재 요청","flagged":true,"dataStatus":"확인필요: 변경항목, 변경일","changedAt":null},{"id":"H-034","ticketKey":"BTVB-3014","summary":"[설정] '자녀 안심 설정' 시 콘텐츠 단위 포스터 노출 제어 고도","flagged":true,"dataStatus":"확인필요: 변경항목, 변경일","changedAt":null},{"id":"H-035","ticketKey":"BTVB-3041","summary":"전체 화면 가격 표기 부가세 포함가로 통일","flagged":true,"dataStatus":"확인필요: 변경항목, 변경일","changedAt":null},{"id":"H-036","ticketKey":"BTVB-3158","summary":"SK Pay 명칭 변경 및 결제 플로우 개선 검토","flagged":true,"dataStatus":"확인필요: 변경항목, 변경일","changedAt":null},{"id":"H-037","ticketKey":"BTVB-3069","summary":"[시놉시스/재생화면] 시놉 일원화 및 바로 재생 정책 개선","flagged":true,"dataStatus":"확인필요: 변경항목, 변경일","changedAt":null},{"id":"H-0038","ticketKey":"BTVB-3257","summary":"[RACE] 오늘 핫한 콘텐츠 RACE import(CCF/PVR)","flagged":false,"changeField":"Status","before":"신규","after":"접수완료","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-01","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0039","ticketKey":"BTVB-3256","summary":"AI 커머스광고 채널 확대 대응 개발","flagged":false,"changeField":"Status","before":"사업 검토","after":"접수완료","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-31","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0040","ticketKey":"BTVB-3253","summary":"CATV 소장형 VOD 이용 대상 가입자 상태 확인 기능 검토","flagged":false,"changeField":"Status","before":"신규","after":"진행중","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-01","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0041","ticketKey":"BTVB-3158","summary":"SK Pay 명칭 변경 및 결제 플로우 개선 검토","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-06","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0042","ticketKey":"BTVB-3144","summary":"[재생][인사이드] 인물정보 포커스기반 경량화 및 맥락요약 추가","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0043","ticketKey":"BTVB-3143","summary":"[홈] GNB 메뉴 개편 및 Today B tv 고도화 개발","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0044","ticketKey":"BTVB-3126","summary":"[설정] STB 설정값 현행 적재 요청","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0045","ticketKey":"BTVB-3116","summary":"[체감AI][AI Tip] 제안 접점 확대 및 기타 개선","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-04-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0046","ticketKey":"BTVB-3112","summary":"[체감AI][AI Tip] 알림형 AI Tip 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0047","ticketKey":"BTVB-3104","summary":"[PI][EUXP] 라이브러리 복사 기능 개발 요청(B tv+프리미엄→B tv+)","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0048","ticketKey":"BTVB-3102","summary":"[ZEM/검색] 키즈 앱 딥링크 편성 개발 요청","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0049","ticketKey":"BTVB-3100","summary":"[B tv_EW] 쇼츠(Shorts) 콘텐츠 전용 UI 신규 개발","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0050","ticketKey":"BTVB-3099","summary":"[AI_BM][에이닷] 커머스 가상채널 발화 이동 지원","flagged":false,"changeField":"Status","before":"drop","after":"진행중","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0051","ticketKey":"BTVB-3092","summary":"[체감AI][에이닷] 서비스 에이전트 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0052","ticketKey":"BTVB-3090","summary":"[체감AI][에이닷] 에이닷 서비스 운영 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0053","ticketKey":"BTVB-3086","summary":"[체감AI][에이닷] 실시간 채널 대화 개선","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0054","ticketKey":"BTVB-3080","summary":"[체감AI][에이닷] 미디어 에이전트 검색 결과 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0055","ticketKey":"BTVB-3073","summary":"[체감AI][실시간] DCA 내 추천 채널 제공","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0056","ticketKey":"BTVB-3069","summary":"[시놉시스/재생화면] 시놉 일원화 및 바로 재생 정책 개선","flagged":false,"changeField":"Status","before":"drop","after":"접수완료","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-01","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0057","ticketKey":"BTVB-3068","summary":"[매출][핫딜][홈쇼핑모아보기] 로딩 시간 단축 및 진입 시나리오 개선","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0058","ticketKey":"BTVB-3067","summary":"[매출][핫딜] 타임딜(시간 한정 특가) 운영 위한 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0059","ticketKey":"BTVB-3066","summary":"[매출][홈쇼핑모아보기] 진입 화면 개편","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0060","ticketKey":"BTVB-3063","summary":"[VOD] 음성 언어 통합 상품 및 다중 음성 서비스 제공","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0061","ticketKey":"BTVB-3062","summary":"[실시간] 캐치온 채널 미니EPG 내 '처음부터 보기' 서비스 제공","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0062","ticketKey":"BTVB-3054","summary":"[딥메타]콘텐츠 썸네일 이미지 추출 자동화 개발","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-24","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0063","ticketKey":"BTVB-3051","summary":"[AI_BM][AI 커머스광고] 프로그램 단위 서비스 적용","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0064","ticketKey":"BTVB-3050","summary":"[AI_BM][AI 커머스광고] PPL 데이터 수집 및 연동기능 구현","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0065","ticketKey":"BTVB-3045","summary":"[AD slot] 실시간 채널 마케팅 인벤토리 기능 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0066","ticketKey":"BTVB-3044","summary":"[FAST] 정주행TV 서비스 기능 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0067","ticketKey":"BTVB-3041","summary":"전체 화면 가격 표기 부가세 포함가로 통일","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-23","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0068","ticketKey":"BTVB-3038","summary":"[광고] STB 부팅 On (웜/콜드) 광고 서비스 개발","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-24","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0069","ticketKey":"BTVB-3037","summary":"[매출][핫딜] 샵바이 - EUXP 섹션 상태 갱신 요청","flagged":false,"changeField":"Status","before":"drop","after":"접수완료","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0070","ticketKey":"BTVB-3034","summary":"[광고] 홈 아웃 광고 기능 개발","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-31","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0071","ticketKey":"BTVB-3024","summary":"[스마트알림] 자동 발송되는 시스템 알림 내 마케팅 문구 추가 노출","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-07-21","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0072","ticketKey":"BTVB-3014","summary":"[설정] '자녀 안심 설정' 시 콘텐츠 단위 포스터 노출 제어 고도화","flagged":false,"changeField":"Status","before":"drop","after":"보류(DROP)","reason":null,"impact":null,"deciders":null,"changedAt":"2026-08-20","evidenceUrl":null,"registrant":null,"dataStatus":"정상"},{"id":"H-0073","ticketKey":"BTVB-3253","summary":"CATV 소장형 VOD 이용 대상 가입자 상태 확인 기능 검토","flagged":false,"changeField":"Status","before":"진행중","after":"기술 검토","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-02","evidenceUrl":null,"registrant":null,"dataStatus":null},{"id":"H-0074","ticketKey":"BTVB-3235","summary":"모바일 B tv 리모컨 개선을 위한 STB 연계 기능 개발","flagged":false,"changeField":"Status","before":"사업 검토","after":"기술 검토","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-03","evidenceUrl":null,"registrant":null,"dataStatus":null},{"id":"H-0075","ticketKey":"BTVB-3225","summary":"[체감AI][에이닷] AI 홈 오퍼링 및 UI 일부 개선","flagged":false,"changeField":"Status","before":"진행중","after":"기술 검토","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-03","evidenceUrl":null,"registrant":null,"dataStatus":null},{"id":"H-0076","ticketKey":"BTVB-3211","summary":"[ZEM] My > 마음친구 연결 Tab 삭제","flagged":false,"changeField":"Status","before":"진행중","after":"기술 검토","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-02","evidenceUrl":null,"registrant":null,"dataStatus":null},{"id":"H-0077","ticketKey":"BTVB-3176","summary":"시네패스 서비스 Fade-out","flagged":false,"changeField":"Status","before":"진행중","after":"기술 검토","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-02","evidenceUrl":null,"registrant":null,"dataStatus":null},{"id":"H-0078","ticketKey":"BTVB-3174","summary":"[B tv+] UI 노출 정책 개선","flagged":false,"changeField":"Status","before":"진행중","after":"기술 검토","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-03","evidenceUrl":null,"registrant":null,"dataStatus":null},{"id":"H-0079","ticketKey":"BTVB-3158","summary":"SK Pay 명칭 변경 및 결제 플로우 개선 검토","flagged":false,"changeField":"Status","before":"보류(DROP)","after":"HOLD","reason":null,"impact":null,"deciders":null,"changedAt":"2026-09-02","evidenceUrl":null,"registrant":null,"dataStatus":null}];

/* Header subtitle date: max(masterUpdatedMax, releaseUpdatedMax, milestoneUpdatedMax)
   per handover doc section 2 -- computed from KB meta rather than hardcoded at deploy time. */
(function setHeaderUpdatedDate(){
  const el = document.getElementById('headerUpdatedDate');
  if(!el || !DATA.meta) return;
  const dates = [DATA.meta.masterUpdatedMax, DATA.meta.releaseUpdatedMax, DATA.meta.milestoneUpdatedMax].filter(Boolean);
  if(dates.length) el.textContent = dates.reduce((a,b) => (b > a ? b : a));
})();

// KB의 일부 행(주로 Drop 처리된 일감)은 jiraUrl 셀이 비어 있는 채로 export되어 있다.
// 실제로 값이 채워진 34건은 예외 없이 전부 "https://jira.skbroadband.com/browse/<Jira Key>"
// 패턴이므로, jiraUrl이 비어 있어도 Jira Key 자체는 항상 존재하는 실제 데이터이기 때문에
// 같은 규칙으로 링크를 만들어 채워도 값을 추측/조작하는 것이 아니다. 어떤 일감도 "Jira에서
// 열기" 링크가 누락되지 않도록 로드 시점에 한 번만 보정한다.
(function fillMissingJiraUrls(){
  const JIRA_BASE = 'https://jira.skbroadband.com/browse/';
  DATA.tickets.forEach(t => { if(!t.jiraUrl && t.key) t.jiraUrl = JIRA_BASE + t.key; });
})();

const ALERT_TRIANGLE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 9v4M12 17h.01M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0Z"/></svg>';
const INFO_CIRCLE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><line x1="12" y1="11" x2="12" y2="16"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>';

/* ==================================================================
   관리자 수동 입력 영역 (ADMIN_NOTES)
   ------------------------------------------------------------------
   KB 업로드 런북으로 자동 갱신되는 DATA와 달리, 아래 값들은 관리자가
   이 파일을 열어 직접 텍스트를 채워 넣어 관리합니다. KB 갱신 런북에
   따라 DATA(및 DATA.history)를 교체하더라도 이 블록은 그대로 유지하고
   손대지 마세요 — 값을 null로 두면 대시보드에는 "관리자 입력 예정"
   placeholder가 표시됩니다.
   ================================================================== */
const ADMIN_NOTES = {
  // 지난 미디어 사업-기술 협의체 회의록 아웃링크
  pastCouncilMinutesUrl: 'https://confluence.skbroadband.com/x/kbPJD',
  pastCouncilMinutesLabel: '지난 미디어 사업-기술 협의체 회의록',
  // "주요 일정" 섹션(다음 월간검토·미디어 사업-기술 협의체 일정 등) — 자유 텍스트(줄바꿈 가능)
  nextReviewSchedule: null,
};

function renderAdminNotes(){
  const placeholder = (msg) => `<div class="info-card placeholder">${INFO_CIRCLE_ICON}<span>${esc(msg)}</span></div>`;

  // 지난 협의체 회의록: 전용 섹션 대신 플로팅 FAB 배너로 제공 — URL이 없으면 숨긴다.
  const councilFab = document.getElementById('councilFab');
  if(councilFab){
    if(ADMIN_NOTES.pastCouncilMinutesUrl){
      councilFab.href = ADMIN_NOTES.pastCouncilMinutesUrl;
      councilFab.hidden = false;
    } else {
      councilFab.hidden = true;
    }
  }

  const scheduleEl = document.getElementById('nextScheduleCard');
  if(scheduleEl){
    scheduleEl.innerHTML = ADMIN_NOTES.nextReviewSchedule
      ? `<div class="info-card"><div class="v">${esc(ADMIN_NOTES.nextReviewSchedule).replace(/\n/g,'<br>')}</div></div>`
      : placeholder('등록된 일정이 없습니다. 관리자 입력 예정입니다.');
  }
}
renderAdminNotes();

/* ==================================================================
   BR 작성 가이드라인 — 업로드된 BR_guidline.pdf 원문을 드로어에서
   보여주기 좋게 요약/정리한 정적 콘텐츠 (KB 데이터 아님)
   ================================================================== */
const BR_GUIDE_HTML = `
  <div class="br-guide-section">
    <p><b>BR(Business Request)</b>은 사업 부서의 요구사항을 개발 부서에 상세하게 전달하기 위한 Jira 문서 형식입니다. 사업 기획 의도와 개발 요구사항을 이해·전달하고, 관련 부서와 공유하며, 개발 완료까지의 가드레일이자 프로젝트 진행 관리 수단으로 사용됩니다.</p>
    <p style="color:var(--ink-faint); font-size:12px;">형식: Jira <b>B tv 개발(BTVB)</b> 프로젝트 · Issue Type: <b>BR</b> · 작성: B tv 서비스기획팀 · 작성 예시 BTVB-2932</p>
  </div>
  <div class="br-guide-section">
    <h4>Summary 작성 규칙</h4>
    <p>15~25자 내외, 구체적이고 명시적인 단어로 작성합니다. 맨 앞에 <span class="mono">[서비스영역]</span> 대괄호 표기 후 "무엇을 + 어떻게 + 왜" 순서로 간결하게 씁니다.</p>
    <p style="color:var(--ink-faint);">예시: <s>[구매] 모니터링을 위한 구매 테이블 프로필ID 적재</s> → <b>[구매 데이터] 구매 테이블 프로필 ID 적재 요청</b></p>
  </div>
  <div class="br-guide-section">
    <h4>필수 작성 항목</h4>
    <ul>
      <li>Reporter(등록 담당자) · Label('CO' 선택, 모바일 개발 건은 '모바일 B tv' 추가)</li>
      <li>KPI 연동 여부(연동/무관) · 예산 확보 여부(확보/미확보)</li>
      <li><b>Business Rationale</b> — 발의부서, 사업 배경 및 근거(당위성·목적 세 문장 내외 + 관련자료 첨부), 기타(재개 건·정부/행정 지침 건 명기), 현황(신규 서비스 vs 기존 서비스 개선에 따라 기재 항목 상이)</li>
      <li><b>개발 Request</b> — 개요(왜/어디를/무엇을/어떻게), 개발 요청사항 상세(As-Is → To-Be, 시나리오 case별 기재, 순서도·wireframe·menu tree 등 시각자료 활용), Log(수집항목·리포팅), 운영 정책, 예상 고객 Side 영향도</li>
      <li><b>Appendix</b> — Customer Value, User Flow, 정량 target(가능한 수치화), Attachments, Assignee(B tv AX팀 기본, 타팀 발의 시 assignee=팀내 담당자·reporter=발의팀)</li>
    </ul>
  </div>
  <div class="br-guide-section">
    <h4>작성 Rule</h4>
    <ul>
      <li>사업부서 모든 구성원이 작성 가능합니다.</li>
      <li>Btv서비스기획팀 검토가 필요하면 지정담당자가 보강하거나 작성자에게 보강을 요청합니다(컨센서스 필요).</li>
      <li>Btv서비스기획팀 관리만 필요한 건은 PMO(윤자연·이설화 매니저)를 통해 관리대상으로 list-up하고, 작성/보강은 해당팀(AIX·모바일 B tv·키즈·Race 한정)이 자체 진행합니다.</li>
    </ul>
  </div>
  <div class="br-guide-section">
    <h4>Status 흐름</h4>
    <div class="br-guide-flow">
      <span class="step">신규 (조율·보강중)</span><span class="arrow">→</span>
      <span class="step">사업 검토 (BR 업데이트 완료)</span><span class="arrow">→</span>
      <span class="step">진행중 (CR 작성)</span><span class="arrow">→</span>
      <span class="step">CR 이관 (접수 완료)</span>
    </div>
    <p style="margin-top:8px;">'진행중' 단계 이후 내용을 변경·삭제할 때는 반드시 댓글로 고지해야 합니다. 삭제는 내용을 지우지 않고 취소선으로 이력을 남기고, 일부 변경 시 컬러 텍스트로 변경 부분을 표시하는 것을 권장합니다.</p>
  </div>
  <div class="br-guide-section" style="color:var(--ink-faint); font-size:11.5px;">이 내용은 BR_guidline.pdf 원문의 핵심을 정리한 요약입니다. 세부 작성 시 원본 가이드라인을 함께 참고하세요.</div>
`;
function openBrGuideDrawer(){
  document.getElementById('drawerKind').textContent = 'Guide';
  document.getElementById('drawerTitle').innerHTML = 'BR 작성 가이드라인';
  document.getElementById('drawerBody').innerHTML = BR_GUIDE_HTML;
  openDrawer();
}
(function bindBrGuideBtn(){
  const btn = document.getElementById('brGuideBtn');
  if(btn) btn.addEventListener('click', openBrGuideDrawer);
})();

/* ==================================================================
   2탭 구조 (프로젝트 진행 현황 / 일감 관리) 전환
   ================================================================== */
(function initTabs(){
  const btns = Array.from(document.querySelectorAll('.tab-btn'));
  const panels = { progress: document.getElementById('tab-progress'), tickets: document.getElementById('tab-tickets') };
  if(!btns.length) return;
  btns.forEach(b => {
    b.addEventListener('click', () => {
      const key = b.dataset.tab;
      btns.forEach(x => x.classList.toggle('active', x === b));
      Object.entries(panels).forEach(([k, el]) => { if(el) el.hidden = (k !== key); });
    });
  });
})();

function historyEntriesFor(key){
  return (DATA.history || [])
    .filter(h => h.ticketKey === key)
    .slice()
    .sort((a,b) => (b.changedAt || '') < (a.changedAt || '') ? -1 : ((b.changedAt||'') > (a.changedAt||'') ? 1 : 0));
}

function renderHistorySection(t){
  const entries = historyEntriesFor(t.key);
  if(entries.length === 0) return '';

  const mismatchNote = t.statusFromHistory
    ? `<div class="data-note">${ALERT_TRIANGLE_ICON}<div>KB 로데이터 상 상태(<b>${esc(t.masterStatus)}</b>)와 히스토리 상 최종 상태(<b>${esc(STATUS_META[t.status]?.label || t.status)}</b>)가 달라, 히스토리를 기준으로 표시하고 있습니다.</div></div>`
    : '';

  const items = entries.map(h => {
    if(h.flagged){
      return `
      <div class="history-item flagged">
        <div class="h-head">
          <span class="h-change">${ALERT_TRIANGLE_ICON} 데이터 확인 필요</span>
          <span class="h-time">${esc(h.id)}</span>
        </div>
        <div class="h-reason na">원본 KB 히스토리 시트에 변경항목·변경일 등 일부 정보가 누락되어 있어, 근거를 표시할 수 없습니다.</div>
      </div>`;
    }
    const metaParts = [];
    if(h.deciders) metaParts.push(`협의체: ${esc(h.deciders)}`);
    if(h.registrant) metaParts.push(`등록: ${esc(h.registrant)}`);
    if(h.evidenceUrl) metaParts.push(`<a href="${esc(h.evidenceUrl)}" target="_blank" rel="noopener">근거 링크 ↗</a>`);
    return `
    <div class="history-item">
      <div class="h-head">
        <span class="h-change">${esc(h.before || '-')} <span class="arrow">→</span> ${statusBadge(h.after)}</span>
        <span class="h-time">${fmtDate(h.changedAt)}</span>
      </div>
      <div class="h-reason${h.reason ? '' : ' na'}">${h.reason ? esc(h.reason) : '변경사유 미기재'}</div>
      ${metaParts.length ? `<div class="h-meta">${metaParts.join('')}</div>` : ''}
    </div>`;
  }).join('');

  return `
    <hr class="dv">
    <div class="history-section">
      <div class="history-section-head"><h3>상태 변경 이력</h3><span class="cnt">${entries.length}건</span></div>
      ${mismatchNote}
      <div class="history-list">${items}</div>
    </div>
  `;
}

/* ---------------- helpers ---------------- */
const $ = (sel, el=document) => el.querySelector(sel);
const $$ = (sel, el=document) => Array.from(el.querySelectorAll(sel));
const TODAY = new Date(); TODAY.setHours(0,0,0,0); // live clock, read once at render time
function fmtJSDate(d){ return `${d.getFullYear()}.${String(d.getMonth()+1).padStart(2,'0')}.${String(d.getDate()).padStart(2,'0')}`; }
function daysBetween(a,b){ return Math.round((b-a)/86400000); }

function parseDate(v){
  if(v == null) return null;
  if(typeof v === 'object' && v.invalid) return null;
  const [y,m,d] = v.split('-').map(Number);
  return new Date(y, m-1, d);
}
function isInvalid(v){ return v != null && typeof v === 'object' && v.invalid; }
function fmtDate(v){
  if(v == null) return '-';
  if(isInvalid(v)) return v.raw + ' ⚠';
  const dt = parseDate(v);
  return `${dt.getFullYear()}.${String(dt.getMonth()+1).padStart(2,'0')}.${String(dt.getDate()).padStart(2,'0')}`;
}
function fmtDateShort(v){
  if(v == null || isInvalid(v)) return '-';
  const dt = parseDate(v);
  return `${String(dt.getMonth()+1).padStart(2,'0')}/${String(dt.getDate()).padStart(2,'0')}`;
}
function esc(s){
  if(s == null) return '';
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
function naSpan(v, cls){
  return v ? `<span class="v ${cls||''}">${esc(v)}</span>` : `<span class="v na">-</span>`;
}

const STATUS_META = {
  '신규':      {c:'--st-new',      soft:'--st-new-soft',      label:'신규'},
  '접수완료':   {c:'--st-received', soft:'--st-received-soft', label:'CR 이관'},
  '사업 검토':  {c:'--st-review',   soft:'--st-review-soft',   label:'사업 검토'},
  '진행중':    {c:'--st-progress', soft:'--st-progress-soft', label:'진행중'},
  '기술 검토':  {c:'--st-tech',     soft:'--st-tech-soft',     label:'기술 검토'},
  'drop':     {c:'--st-drop',     soft:'--st-drop-soft',     label:'Drop'},
  '보류(DROP)': {c:'--st-drop',    soft:'--st-drop-soft',     label:'보류(DROP)'},
  'HOLD':     {c:'--st-drop',     soft:'--st-drop-soft',     label:'HOLD'},
};
// 2026-09 KB부터 원천 상태값이 세분화됨: 진행중/사업 검토 중 일부가 "기술 검토"로,
// drop이 "보류(DROP)"→"HOLD" 순으로 전환 중(마이그레이션 진행 중이라 세 값이 혼재).
// 데이터를 임의로 합치지 않고 원본 문자열 그대로 별도 칼럼으로 노출한다.
const STATUS_ORDER = ['신규','사업 검토','기술 검토','진행중','접수완료','drop','보류(DROP)','HOLD'];

/* ---------------- history-based status override ----------------
   히스토리(04.project_agent_history) 시트의 최신 상태 변경 이력이 있고,
   그 상태값이 로데이터(마스터) 상태와 다를 경우, 히스토리를 기준으로
   화면에 표시한다. 원본 마스터 상태는 t.masterStatus 에 보존한다. */
(function applyHistoryStatusOverrides(){
  const latestByKey = {};
  (DATA.history || []).forEach(h => {
    if(h.flagged || !h.changeField || h.changeField !== 'Status') return;
    if(!h.after || !STATUS_ORDER.includes(h.after)) return;
    const prev = latestByKey[h.ticketKey];
    if(!prev || (h.changedAt || '') >= (prev.changedAt || '')){
      latestByKey[h.ticketKey] = h;
    }
  });
  DATA.tickets.forEach(t => {
    const latest = latestByKey[t.key];
    if(latest && latest.after !== t.status){
      t.masterStatus = t.status;
      t.status = latest.after;
      t.statusFromHistory = true;
    }
  });
})();

function statusBadge(status){
  const m = STATUS_META[status] || {c:'--ink-faint', soft:'--surface-2', label:status||'-'};
  return `<span class="badge" style="background:var(${m.soft});color:var(${m.c})">${esc(m.label)}</span>`;
}

/* ---------------- change history (전체 변경이력) ---------------- */
// 04.project_agent_history 시트의 모든 상태 변경 이력을 최근순으로 한 번에 보여주는 표.
// "근거" 컬럼은 KB의 변경사유(reason)가 아니라 의사결정자/협의체(deciders) 값을 표시한다.
function renderChangeHistoryTable(){
  const tbody = document.getElementById('changeHistoryBody');
  if(!tbody) return;
  const idNum = (id) => { const m = String(id||'').match(/(\d+)/); return m ? parseInt(m[1],10) : -1; };
  const entries = (DATA.history || []).slice()
    .sort((a, b) => idNum(b.id) - idNum(a.id))
    .slice(0, 20);
  tbody.innerHTML = entries.map(h => {
    const t = DATA.tickets.find(x => x.key === h.ticketKey);
    const changeHtml = (h.flagged || !h.changeField)
      ? `<span class="ch-change na">${ALERT_TRIANGLE_ICON} 데이터 확인 필요</span>`
      : `<span class="ch-change">${esc(h.before || '-')} <span class="arrow">→</span> ${statusBadge(h.after)}</span>`;
    return `
      <tr data-key="${esc(h.ticketKey)}">
        <td class="ch-ticket"><span class="k">${esc(h.ticketKey)}</span><span class="s">${esc(h.summary || (t && t.summary) || '-')}</span></td>
        <td>${changeHtml}</td>
        <td class="mono ch-date">${h.changedAt ? fmtDate(h.changedAt) : '-'}</td>
        <td class="${h.deciders ? '' : 'na'}">${h.deciders ? esc(h.deciders) : ''}</td>
      </tr>
    `;
  }).join('');
  tbody.querySelectorAll('tr').forEach(row => {
    row.addEventListener('click', () => {
      const t = DATA.tickets.find(x => x.key === row.dataset.key);
      if(t) openTicketDrawer(t);
    });
  });
}
renderChangeHistoryTable();

const VERSION_COLORS = {
  '5.6.1':    {main:'#4A5DAE', soft:'#E4E7F5'},
  '5.6.1 #1': {main:'#8B5FA3', soft:'#EFE6F2'},
  '5.6.1 #2': {main:'#0C7489', soft:'#DCEEF1'},
  '5.6.2':    {main:'#A9740F', soft:'#F3E7CC'},
};
function verColor(v){ return VERSION_COLORS[v] || {main:'#7C8F89', soft:'#E4EBE8'}; }

/* ---------------- person / org parsing ---------------- */
// Reporter & Assignee are stored as "이름/조직명" — split once so org becomes a first-class,
// filterable field instead of buried inside a free-text string.
function personParts(raw){
  if(!raw) return {name:null, org:null};
  const i = raw.indexOf('/');
  if(i === -1) return {name:raw, org:null};
  return {name: raw.slice(0,i).trim(), org: raw.slice(i+1).trim()};
}
DATA.tickets.forEach(t => {
  const rp = personParts(t.reporter), ap = personParts(t.assignee);
  t.reporterName = rp.name; t.reporterOrg = rp.org;
  t.assigneeName = ap.name; t.assigneeOrg = ap.org;
});
/* ---------------- stats ---------------- */
// Same "만료된 레인 제외" 규칙을 renderRunway와 공유(중복 정의) — 다음 마일스톤 칩이 항상
// 마일스톤 타임라인에 실제로 보이는 레인과 일치하도록 한다.
function activeMilestoneLanes(){
  const addMonths = (d, n) => { const r = new Date(d); r.setMonth(r.getMonth() + n); return r; };
  const isLaneExpired = (version) => {
    const finishes = DATA.milestones
      .filter(m => m.version === version)
      .map(m => parseDate(m.finish))
      .filter(Boolean);
    if(!finishes.length) return false;
    const maxFinish = finishes.reduce((a, b) => (b > a ? b : a));
    return addMonths(maxFinish, 1) < TODAY;
  };
  return ['5.6.1','5.6.1 #2','5.6.2'].filter(v => !isLaneExpired(v)).sort(compareVersionDesc);
}

(function renderStats(){
  const tickets = DATA.tickets;
  const byStatus = {};
  tickets.forEach(t => byStatus[t.status] = (byStatus[t.status]||0) + 1);

  // next upcoming release (due date >= today, excluding invalid), fallback to closest overall
  const releasesSorted = DATA.releases
    .map(r => ({r, d: parseDate(r.dueDate)}))
    .filter(x => x.d)
    .sort((a,b) => a.d - b.d);
  const nextRelease = releasesSorted.find(x => x.d >= TODAY) || releasesSorted[releasesSorted.length-1];

  // next upcoming milestone, per active runway lane (5.6.2 / 5.6.1 #2 등 — 만료되지 않은 레인만)
  const nextMsByLane = activeMilestoneLanes().map(lane => {
    const sorted = DATA.milestones
      .filter(m => m.version === lane)
      .map(m => ({m, d: parseDate(m.start)}))
      .filter(x => x.d && x.d >= TODAY)
      .sort((a,b) => a.d - b.d);
    return {lane, next: sorted[0] || null};
  });

  // "기술 검토"는 2026-09 KB부터 진행중(주로)·사업 검토(일부)를 승계하는 새 상태명이라
  // 기존에 같은 이름으로 표시되던 타일에 합산한다. Drop 계열(drop/보류(DROP)/HOLD)도
  // 순차 전환 중인 같은 상태의 다른 시점 라벨이라 한 타일로 합산한다.
  const sumStatuses = (list) => list.reduce((n, st) => n + (byStatus[st]||0), 0);
  const stats = [
    {key:'all',      n: tickets.length, l:'전체 일감', small:'1년 이내 발의 일감', statuses:null},
    {key:'review',   n: byStatus['사업 검토']||0, l:'사업 검토', small:'Btv서비스기획 담당 검토', statuses:['사업 검토']},
    {key:'progress', n: sumStatuses(['진행중','기술 검토']), l:'기술 검토', small:'미디어 Tech 검토', statuses:['진행중','기술 검토']},
    {key:'received', n: byStatus['접수완료']||0, l:'CR 이관', small:'CR 작성 및 개발 리소스 검토', statuses:['접수완료']},
    {key:'new',      n: byStatus['신규']||0, l:'신규 작성', small:'검토 대기열', statuses:['신규']},
    {key:'drop',     n: sumStatuses(['drop','보류(DROP)','HOLD']), l:'Drop', small:'반영 제외/보류', statuses:['drop','보류(DROP)','HOLD']},
  ];
  $('#stats').innerHTML = stats.map(s => `
    <div class="stat clickable ${s.accent?'accent':''}" data-tile-key="${s.key}" tabindex="0" role="button"
         aria-label="${esc(s.l)} 일감 목록 보기">
      <div class="n">${s.n}</div>
      <div class="l">${s.l}<small>${s.small}</small></div>
    </div>
  `).join('');
  $$('.stat.clickable', $('#stats')).forEach((el, i) => {
    const s = stats[i];
    const activate = () => openStatusDrawer(s.statuses, s.l);
    el.addEventListener('click', activate);
    el.addEventListener('keydown', e => { if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); activate(); } });
  });

  // "다음 마일스톤 / 다음 배포" 하이라이트 카드 — 눈에 잘 띄도록 큰 카드 형태로 표시
  // (구 버전: 작은 pill 칩 리스트). 회의체 아웃링크는 여기 포함하지 않고 별도의
  // 플로팅 배너(FAB)로 제공한다.
  const ICON_CALENDAR = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>';
  const ICON_LAYERS = '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 3 7l9 5 9-5-9-5z"/><path d="M3 12l9 5 9-5"/><path d="M3 17l9 5 9-5"/></svg>';

  const msCardsHtml = nextMsByLane.map(({lane, next}) => `
    <div class="next-up-card milestone">
      ${ICON_CALENDAR}
      <div class="label">다음 마일스톤 · ${esc(lane)}</div>
      <div class="desc">${next ? esc(next.m.name) : '예정된 마일스톤이 없습니다'}</div>
      <div class="date">${next ? fmtDate(next.m.start) + ' 시작' : '확인되지 않음'}</div>
    </div>
  `).join('');
  const deployDesc = nextRelease
    ? `${esc(nextRelease.r.version)} ${esc(nextRelease.r.group)} · ${esc(nextRelease.r.status||'-')}`
    : '확인되지 않음';
  const deployDate = nextRelease ? fmtDate(nextRelease.r.dueDate) : '확인되지 않음';
  const deployCardHtml = `
    <div class="next-up-card deploy">
      ${ICON_LAYERS}
      <div class="label">다음 배포</div>
      <div class="desc">${deployDesc}</div>
      <div class="date">${deployDate}</div>
    </div>
  `;
  const grid = document.createElement('div');
  grid.className = 'next-up-grid';
  grid.innerHTML = `${msCardsHtml}${deployCardHtml}`;
  // stat 타일은 "일감 관리" 탭으로 이동했지만, 다음 마일스톤/다음 배포 카드는 "프로젝트
  // 진행 현황" 탭의 마일스톤 타임라인 위쪽에 그대로 유지한다 (정적 슬롯에 삽입).
  const slot = document.getElementById('nextUpBarSlot');
  if(slot) slot.replaceWith(grid); else $('#stats').after(grid);
})();

/* ---------------- runway ---------------- */
/* ---------------- current-stage summary (date-driven, not milestone counts) ---------------- */
function stageForVersion(version){
  const items = DATA.milestones.filter(m => m.version === version)
    .map(m => ({m, s: parseDate(m.start), f: (!isInvalid(m.finish) && parseDate(m.finish)) || parseDate(m.start)}))
    .filter(x => x.s);
  return {
    active: items.filter(x => x.s <= TODAY && TODAY <= x.f),
    upcoming: items.filter(x => x.s > TODAY).sort((a,b) => a.s - b.s),
    past: items.filter(x => x.f < TODAY).sort((a,b) => b.f - a.f),
  };
}
// Computes the "current stage" badge/headline/date-range for a version — now shown
// inline in the timeline's own lane label instead of a separate row of tiles above it,
// so the version identity and its current stage live in one visual block.
function stageInfoFor(version){
  const {active, upcoming, past} = stageForVersion(version);
  let badge, headline, sub;
  if(active.length){
    const maxFinishItem = active.reduce((m,x) => x.f > m.f ? x : m, active[0]);
    const minStartItem  = active.reduce((m,x) => x.s < m.s ? x : m, active[0]);
    const names = active.map(x => x.m.name);
    badge = `<span class="stage-badge" style="background:var(--st-progress-soft);color:var(--st-progress)">진행중 · ${active.length}건</span>`;
    headline = names.slice(0,2).join(' · ') + (names.length > 2 ? ` 외 ${names.length-2}건` : '');
    const endLabel = isInvalid(maxFinishItem.m.finish) ? maxFinishItem.m.finish.raw + ' ⚠' : fmtJSDate(maxFinishItem.f);
    sub = `${fmtJSDate(minStartItem.s)} ~ ${endLabel}`;
  } else if(upcoming.length){
    const dstart = daysBetween(TODAY, upcoming[0].s);
    badge = `<span class="stage-badge" style="background:var(--st-new-soft);color:var(--st-new)">다음 단계</span>`;
    headline = upcoming[0].m.name;
    sub = `D-${dstart} · ${fmtJSDate(upcoming[0].s)} 시작 예정`;
  } else if(past.length){
    badge = `<span class="stage-badge" style="background:var(--surface-3);color:var(--ink-faint)">예정된 일정 없음</span>`;
    headline = past[0].m.name;
    sub = '';
  } else {
    badge = `<span class="stage-badge" style="background:var(--surface-3);color:var(--ink-faint)">정보 없음</span>`;
    headline = '등록된 마일스톤 없음';
    sub = '';
  }
  return {badge, headline, sub};
}

// Maps a milestone-timeline lane version (e.g. "5.6.1") to the matching release
// rows in DATA.releases. Some KB exports have named an early release round with a
// "#N" suffix (e.g. "5.6.1 #1") even though the milestone sheet uses the bare
// version — this reconciles that mismatch generically, falling back to the
// lowest-numbered "#N" round for a bare lane version when no exact match exists.
function releasesForLaneVersion(lane){
  const laneBase = baseVersionForMatch(lane);
  const laneSuffixMatch = String(lane).match(/#(\d+)/);
  const laneSuffix = laneSuffixMatch ? parseInt(laneSuffixMatch[1], 10) : null;
  const candidates = DATA.releases.filter(r => baseVersionForMatch(r.version) === laneBase);
  if(laneSuffix != null){
    return candidates.filter(r => {
      const m = String(r.version).match(/#(\d+)/);
      return (m ? parseInt(m[1], 10) : null) === laneSuffix;
    });
  }
  // Bare lane version (no "#N"): prefer an exact bare match if the KB has one,
  // otherwise fall back to the lowest-numbered round for this base version.
  const exact = candidates.filter(r => !/#\d+/.test(String(r.version)));
  if(exact.length) return exact;
  const withSuffix = candidates
    .map(r => ({ r, s: parseInt((String(r.version).match(/#(\d+)/) || [])[1], 10) }))
    .filter(x => !isNaN(x.s))
    .sort((a, b) => a.s - b.s);
  if(!withSuffix.length) return [];
  return withSuffix.filter(x => x.s === withSuffix[0].s).map(x => x.r);
}

// A version's timeline lane is shown as fully deployed only when EVERY one of its
// matched release-group rows has the explicit KB status "배포완료" (not "상시배포",
// not "배포예정", not missing) — never inferred from dates alone.
function releaseCompletionInfo(lane){
  const matches = releasesForLaneVersion(lane);
  if(!matches.length || !matches.every(r => r.status === '배포완료')) return null;
  const dates = matches.map(r => parseDate(r.dueDate)).filter(Boolean);
  const maxDate = dates.length ? dates.reduce((a, b) => (b > a ? b : a)) : null;
  const headline = matches.length > 1
    ? `${matches.length}개 그룹 배포 완료`
    : `${matches[0].group} 배포 완료`;
  return {
    badge: `<span class="stage-badge" style="background:var(--st-progress-soft);color:var(--st-progress)">배포 완료</span>`,
    headline,
    sub: maxDate ? `배포일 ${fmtJSDate(maxDate)}` : '',
  };
}

(function renderRunway(){
  // 마일스톤 종료일(유효한 날짜만) 기준으로 최근 종료일이 오늘로부터 1개월 이상 지난 버전은
  // 타임라인에서 제외한다. 유효한 종료일이 하나도 없는 버전은 판단할 근거가 없으므로 그대로 둔다.
  const addMonths = (d, n) => { const r = new Date(d); r.setMonth(r.getMonth() + n); return r; };
  const isLaneExpired = (version) => {
    const finishes = DATA.milestones
      .filter(m => m.version === version)
      .map(m => parseDate(m.finish))
      .filter(Boolean);
    if(!finishes.length) return false;
    const maxFinish = finishes.reduce((a, b) => (b > a ? b : a));
    return addMonths(maxFinish, 1) < TODAY;
  };
  const lanes = ['5.6.1','5.6.1 #2','5.6.2'].filter(v => !isLaneExpired(v)).sort(compareVersionDesc);
  const legend = document.getElementById('runwayLegend');
  legend.innerHTML = lanes.map(v => {
    const c = verColor(v);
    return `<span class="lg"><span class="sw" style="background:${c.main}"></span>${v}</span>`;
  }).join('')
    + `<span class="lg"><span class="sw" style="background:none;outline:2px solid var(--ink);width:9px;height:9px"></span>진행중인 단계</span>`
    + `<span class="lg"><span class="sw" style="background:var(--surface-2);border:1.5px dashed var(--ink-faint)"></span>예정 단계 (시작 전)</span>`
    + `<span class="lg"><span class="sw" style="background:var(--ink-faint);opacity:.4"></span>지난 단계</span>`;

  // compute global range from valid dates
  let minD = null, maxD = null;
  DATA.milestones.forEach(m => {
    const s = parseDate(m.start), f = parseDate(m.finish);
    if(s && (!minD || s < minD)) minD = s;
    if(s && (!maxD || s > maxD)) maxD = s;
    if(f && (!maxD || f > maxD)) maxD = f;
  });
  // pad range by ~5% on each side
  const rangeMs = maxD - minD;
  const pad = rangeMs * 0.03;
  const rangeStart = new Date(minD.getTime() - pad);
  const rangeEnd = new Date(maxD.getTime() + pad);
  const totalMs = rangeEnd - rangeStart;
  const pct = (d) => ((d - rangeStart) / totalMs) * 100;

  const TRACK_WIDTH = 1382; // px, matches runway-inner minus label width roughly

  const inner = document.getElementById('runwayInner');
  const labelsWrap = document.getElementById('runwayLabels');
  inner.innerHTML = '';
  labelsWrap.innerHTML = '<div class="runway-labels-spacer"></div>'; // aligns with the month-header row
  const wideBars = [];

  // month gridlines
  const monthsWrap = document.createElement('div');
  monthsWrap.className = 'runway-months';
  let cursor = new Date(rangeStart.getFullYear(), rangeStart.getMonth(), 1);
  while(cursor <= rangeEnd){
    const p = pct(cursor);
    if(p >= 0){
      const el = document.createElement('div');
      el.className = 'runway-month';
      el.style.left = p + '%';
      el.textContent = `${cursor.getFullYear()}.${String(cursor.getMonth()+1).padStart(2,'0')}`;
      monthsWrap.appendChild(el);
    }
    cursor = new Date(cursor.getFullYear(), cursor.getMonth()+1, 1);
  }
  inner.appendChild(monthsWrap);

  lanes.forEach(version => {
    const items = DATA.milestones.filter(m => m.version === version)
      .map(m => ({m, s: parseDate(m.start), f: parseDate(m.finish) || parseDate(m.start)}))
      .filter(x => x.s)
      .sort((a,b) => a.s - b.s);

    // row packing
    const rows = []; // each: last end date
    items.forEach(item => {
      let placed = false;
      for(let i=0;i<rows.length;i++){
        if(item.s >= rows[i]){
          rows[i] = new Date(item.f.getTime() + 86400000*3);
          item.row = i;
          placed = true;
          break;
        }
      }
      if(!placed){
        rows.push(new Date(item.f.getTime() + 86400000*3));
        item.row = rows.length-1;
      }
    });
    const rowCount = Math.max(rows.length, 1);
    const laneHeight = rowCount * 22 + 12;

    const c = verColor(version);
    const {badge, headline, sub} = releaseCompletionInfo(version) || stageInfoFor(version);

    // Label lives in the frozen #runwayLabels column (not inside the horizontally
    // scrolling #runwayInner) so it can never be scrolled under the timeline bars —
    // its height is set to match this lane's track height exactly, row for row.
    const labelEl = document.createElement('div');
    labelEl.className = 'lane-label';
    labelEl.style.height = laneHeight + 'px';
    labelEl.innerHTML = `
      <div class="lane-label-top"><b style="color:${c.main}">${esc(version)}</b>${badge}</div>
      <div class="lane-label-stage">${esc(headline)}</div>
      ${sub ? `<div class="lane-label-date">${esc(sub)}</div>` : ''}
    `;
    labelsWrap.appendChild(labelEl);

    const lane = document.createElement('div');
    lane.className = 'runway-lane';
    lane.innerHTML = `<div class="lane-track" style="height:${laneHeight}px"></div>`;
    const track = lane.querySelector('.lane-track');

    items.forEach(item => {
      const left = pct(item.s);
      const right = pct(item.f);
      const width = Math.max(right - left, 0);
      const top = item.row * 22 + 6;
      const zeroDuration = (right - left) < 0.3;
      const isCurrent = item.s <= TODAY && TODAY <= item.f;
      // Past = finish date already behind today. This only fades the bar visually —
      // it does not claim "완료" anywhere, since Milestone Status isn't populated in the KB.
      const isPast = !isCurrent && item.f < TODAY;
      // Upcoming = start date still ahead of today — gets a soft-fill/dashed treatment
      // distinct from both the dimmed past state and the solid current state.
      const isUpcoming = !isCurrent && item.s > TODAY;

      if(zeroDuration){
        const dot = document.createElement('div');
        dot.className = 'ms-dot' + (isCurrent ? ' is-current' : '') + (isPast ? ' is-past' : '') + (isUpcoming ? ' is-upcoming' : '');
        dot.style.left = `calc(${left}% - 6px)`;
        dot.style.top = top + 'px';
        dot.style.background = isUpcoming ? c.soft : c.main;
        if(isUpcoming) dot.style.borderColor = c.main;
        dot.title = item.m.name + (isCurrent ? ' (진행중)' : isPast ? ' (지난 일정)' : isUpcoming ? ' (예정)' : '');
        dot.addEventListener('click', () => openMilestoneDrawer(item.m));
        track.appendChild(dot);
      } else {
        const bar = document.createElement('div');
        bar.className = 'ms-bar' + (isInvalid(item.m.finish) ? ' warn-flag' : '') + (isCurrent ? ' is-current' : '') + (isPast ? ' is-past' : '') + (isUpcoming ? ' is-upcoming' : '');
        bar.style.left = left + '%';
        bar.style.width = width + '%';
        bar.style.top = top + 'px';
        bar.style.background = isUpcoming ? c.soft : c.main;
        if(isUpcoming){ bar.style.borderColor = c.main; bar.style.color = c.main; }
        bar.title = item.m.name + (isCurrent ? ' (진행중)' : isPast ? ' (지난 일정)' : isUpcoming ? ' (예정)' : '');
        bar.addEventListener('click', () => openMilestoneDrawer(item.m));
        track.appendChild(bar);
        wideBars.push({el: bar, name: item.m.name});
      }
    });

    inner.appendChild(lane);
  });

  // now that bars are attached to the live DOM, measure actual pixel width to decide labeling
  wideBars.forEach(({el, name}) => {
    const pxWidth = el.getBoundingClientRect().width;
    if(pxWidth < 34){
      el.classList.add('no-label');
    } else {
      el.textContent = name;
    }
  });

  // today line spanning full inner height
  const todayLeft = pct(TODAY);
  const totalHeight = inner.offsetHeight;
  const todayLine = document.createElement('div');
  todayLine.className = 'today-line';
  todayLine.style.left = todayLeft + '%';
  todayLine.style.top = '0';
  todayLine.style.height = inner.scrollHeight + 'px';
  const tag = document.createElement('div');
  tag.className = 'today-tag';
  tag.textContent = `오늘 ${TODAY.getMonth()+1}/${TODAY.getDate()}`;
  todayLine.appendChild(tag);
  inner.style.position = 'relative';
  inner.appendChild(todayLine);

  // default the horizontal scroll so "오늘" line sits centered in the visible viewport,
  // rather than showing the timeline's leftmost (earliest) edge on load.
  const scrollEl = document.querySelector('.runway-scroll');
  if(scrollEl){
    const target = todayLine.offsetLeft - scrollEl.clientWidth / 2;
    scrollEl.scrollLeft = Math.max(0, Math.min(target, scrollEl.scrollWidth - scrollEl.clientWidth));
  }
})();

/* ---------------- releases ---------------- */
function parseVersionForSort(v){
  const s = String(v || '');
  const suffixMatch = s.match(/#(\d+)/);
  const suffix = suffixMatch ? parseInt(suffixMatch[1], 10) : 0;
  const base = s.replace(/#\d+/, '').trim();
  const parts = base.split('.').map(x => parseInt(x, 10) || 0);
  return { parts, suffix };
}
function compareVersionDesc(v1, v2){
  const p1 = parseVersionForSort(v1), p2 = parseVersionForSort(v2);
  const len = Math.max(p1.parts.length, p2.parts.length);
  for(let i = 0; i < len; i++){
    const a = p1.parts[i] || 0, b = p2.parts[i] || 0;
    if(a !== b) return b - a;
  }
  if(p1.suffix !== p2.suffix) return p2.suffix - p1.suffix;
  return 0;
}
function groupNumber(g){
  const m = String(g||'').match(/(\d+)/);
  return m ? parseInt(m[1],10) : 0;
}
(function renderReleases(){
  const grid = document.getElementById('releaseGrid');
  const STATUS_BG = {
    '배포중':'var(--st-received-soft)','상시배포':'var(--st-review-soft)','배포예정':'var(--st-new-soft)','배포완료':'var(--st-progress-soft)'
  };
  const STATUS_FG = {
    '배포중':'var(--st-received)','상시배포':'var(--st-review)','배포예정':'var(--st-new)','배포완료':'var(--st-progress)'
  };
  // 그룹 상태 우선순위: 배포중 > 상시배포 > 배포예정 > 배포완료.
  // 요약 줄과 기본 표시 그룹 모두 이 우선순위를 기준으로 계산한다.
  const STATUS_PRIORITY = { '배포중':4, '상시배포':3, '배포예정':2, '배포완료':1 };
  const STATUS_FOCUS_LABEL = { '배포중':'배포중', '상시배포':'상시 배포', '배포예정':'배포예정', '배포완료':'배포완료' };
  const priorityOf = (status) => STATUS_PRIORITY[status] || 0;

  // Tiles are version-level now (previously one card per version+group row).
  // Each group's status/detail is shown as a compact row inside its version's tile.
  const byVersion = {};
  DATA.releases.forEach(r => { (byVersion[r.version] || (byVersion[r.version] = [])).push(r); });
  const versions = Object.keys(byVersion).sort(compareVersionDesc);

  grid.innerHTML = versions.map(version => {
    const rows = byVersion[version].slice().sort((a, b) => {
      const gn = groupNumber(a.group) - groupNumber(b.group);
      if(gn !== 0) return gn;
      const da = a.dueDate ? new Date(a.dueDate) : null;
      const db = b.dueDate ? new Date(b.dueDate) : null;
      if(da && db) return da - db;
      return 0;
    });
    // 기본으로 보여줄(가장 먼저 노출할) 그룹 결정:
    // 1) status 우선순위: 배포중 > 상시배포 > 배포예정 > 배포완료.
    // 2) 우선순위가 동률인 그룹이 여럿이면: 그 status가 "배포예정"이면 번호가 가장 앞선(빠른) 그룹을,
    //    그 외(배포중/상시배포/배포완료)이면 번호가 가장 뒤선(늦은) 그룹을 기본으로 삼는다.
    const focusMaxPriority = Math.max(...rows.map(r => priorityOf(r.status)));
    const tiedIndices = [];
    rows.forEach((r, i) => { if(priorityOf(r.status) === focusMaxPriority) tiedIndices.push(i); });
    const tiedStatus = rows[tiedIndices[0]].status;
    const focusIdx = tiedStatus === '배포예정' ? tiedIndices[0] : tiedIndices[tiedIndices.length - 1];
    const focusLabel = (r) => STATUS_FOCUS_LABEL[r.status] || esc(r.status || '-');
    // 요약 줄: 기본 그룹 + 바로 다음 번호 그룹까지 최대 2개. 단, 기본 그룹이 마지막 그룹이면 1개만.
    // 예외: 1그룹이 기본 그룹이면서 상태가 "배포예정"이면(=버전 전체가 아직 시작 전) 1그룹만 보여준다.
    const focusIsGroup1Scheduled = groupNumber(rows[focusIdx].group) === 1 && rows[focusIdx].status === '배포예정';
    const summaryParts = [`${esc(rows[focusIdx].group)} ${focusLabel(rows[focusIdx])}`];
    if(!focusIsGroup1Scheduled && focusIdx < rows.length - 1){
      summaryParts.push(`${esc(rows[focusIdx+1].group)} ${focusLabel(rows[focusIdx+1])}`);
    }
    const summaryLine = summaryParts.join(', ');
    // 대상 일감(ticketCount)과 주요 개발 내용(summary)은 같은 버전 내 그룹 간에 항상 동일하므로
    // 그룹별 행이 아니라 버전 타일 레벨에서 한 번만 보여준다. 실제로 값이 갈리거나 비어있는 예외
    // 케이스에서는 값을 추측하지 않되, 버전 타일 크기를 동일하게 유지하기 위해 이 블록 자체는 항상
    // 같은 높이로 렌더링하고 값이 없을 때만 안내 문구로 대체한다(블록을 통째로 생략하지 않음).
    const ticketCounts = new Set(rows.map(r => r.ticketCount ?? null));
    const summaries = new Set(rows.map(r => r.summary || ''));
    const sharedTicketCount = ticketCounts.size === 1 ? rows[0].ticketCount : null;
    const sharedSummary = summaries.size === 1 ? (rows[0].summary || '') : '';
    const sharedMetaHtml = `
      <div class="release-shared-meta">
        <span class="release-shared-count">대상 일감 ${sharedTicketCount != null ? `<b>${sharedTicketCount}건</b>` : `<span class="muted-italic">확인 필요</span>`}</span>
        <div class="release-summary-shared">${sharedSummary ? esc(sharedSummary) : ''}</div>
      </div>
    `;
    const rowsHtml = rows.map(r => `
      <div class="release-group-row" data-key="${esc(r.version)}|${esc(r.group)}">
        <div class="rg-top">
          <div class="rg-left">
            <span class="rg-group">${esc(r.group)}</span>
            ${r.devices ? `<span class="rg-devices">${esc(r.devices)}</span>` : ''}
          </div>
          <span class="badge" style="background:${STATUS_BG[r.status]||'var(--surface-2)'};color:${STATUS_FG[r.status]||'var(--ink-soft)'}">${esc(r.status||'-')}</span>
        </div>
        <div class="rg-meta">
          <span>${(() => { const d = parseDate(r.dueDate); return (d && d < TODAY) ? '배포시작일' : '배포예정일'; })()} <b>${fmtDate(r.dueDate)}</b></span>
        </div>
        <div class="rg-coverage">${(r.status === '배포예정' || r.status === '배포완료') ? '' : `
          <div class="rg-coverage-head">
            <span title="출처: 05.project_agent_ver_release 시트">배포 단말 커버리지</span>
            <span class="pct${r.coveragePct == null ? ' na' : ''}">${r.coveragePct != null ? r.coveragePct.toFixed(1) + '%' : '-'}</span>
          </div>
          <div class="rg-coverage-track"><div class="rg-coverage-fill" style="width:${r.coveragePct != null ? r.coveragePct : 0}%"></div></div>
          <div class="rg-coverage-foot">${r.deployedUnits != null ? r.deployedUnits.toLocaleString('ko-KR') + ' / ' + r.totalUnits.toLocaleString('ko-KR') + '대' : 'KB에 단말 배포 현황이 집계되지 않았습니다'}</div>
        `}</div>
      </div>
    `).join('');
    // 기본으로 보여줄 그룹: 위와 같은 상태 우선순위(상시 배포 > 배포예정 > 배포완료) 기준으로
    // 가장 우선순위가 높은 그룹을 기본값으로 삼는다(동률이면 위 focusIdx와 동일하게 가장 앞선 그룹).
    const defaultIdx = focusIdx;
    // 그룹이 여러 개면 이 영역 안에서 좌우로 넘겨 볼 수 있게 캐러셀로 구성.
    // 타일마다 그룹 수가 달라도 캐러셀은 항상 한 그룹 높이만 차지하므로 버전별 타일 크기가 동일하게 유지된다.
    // 그룹이 1개뿐이어도 점 표시 영역의 높이는 그대로 확보해 타일 크기를 맞추되, 점 자체는 숨긴다.
    const dotsHtml = `
      <div class="release-group-dots"${rows.length > 1 ? '' : ' style="visibility:hidden;"'}>${rows.map((r, i) => `<button type="button" class="release-group-dot${i===defaultIdx?' active':''}" data-idx="${i}" aria-label="${esc(r.group)} 보기"></button>`).join('')}</div>
    `;
    const navBtnsHtml = rows.length > 1 ? `
      <button type="button" class="release-carousel-nav prev" aria-label="이전 그룹">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>
      </button>
      <button type="button" class="release-carousel-nav next" aria-label="다음 그룹">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    ` : '';
    return `
      <div class="release-card" data-default-idx="${defaultIdx}">
        <div class="release-ver-header">
          <div class="release-ver" style="color:${verColor(version).main}">${esc(version)}</div>
          <div class="release-ver-summary">${summaryLine}</div>
        </div>
        ${sharedMetaHtml}
        <div class="release-carousel-wrap">
          <div class="release-group-carousel">${rowsHtml}</div>
          ${navBtnsHtml}
        </div>
        ${dotsHtml}
      </div>
    `;
  }).join('');

  $$('.release-group-row', grid).forEach(row => {
    row.addEventListener('click', () => {
      const [version, group] = row.dataset.key.split('|');
      const r = DATA.releases.find(x => x.version === version && x.group === group);
      if(r) openReleaseDrawer(r);
    });
  });

  $$('.release-card', grid).forEach(card => {
    const carousel = card.querySelector('.release-group-carousel');
    const dots = $$('.release-group-dot', card);
    const rowEls = $$('.release-group-row', card);
    const prevBtn = card.querySelector('.release-carousel-nav.prev');
    const nextBtn = card.querySelector('.release-carousel-nav.next');
    const defaultIdx = parseInt(card.dataset.defaultIdx, 10) || 0;

    // "대상 일감 NN건" 클릭 시, 캐러셀에 현재 보이는 그룹 기준으로 릴리즈 드로어를 연다.
    // 대상 일감 목록(ticketsForRelease)은 버전 단위로 결정되어 같은 버전 내 어느 그룹을
    // 넘겨도 결과가 동일하므로, 어느 그룹이 보이고 있었는지는 결과에 영향을 주지 않는다.
    const countEl = card.querySelector('.release-shared-count');
    if(countEl){
      countEl.classList.add('clickable');
      countEl.tabIndex = 0;
      countEl.setAttribute('role', 'button');
      countEl.setAttribute('aria-label', '대상 일감 목록 보기');
      const openForVisibleGroup = () => {
        const idx = rowEls.length > 1 ? currentIdx() : defaultIdx;
        const row = rowEls[idx] || rowEls[0];
        if(!row) return;
        const [version, group] = row.dataset.key.split('|');
        const r = DATA.releases.find(x => x.version === version && x.group === group);
        if(r) openReleaseDrawer(r);
      };
      countEl.addEventListener('click', openForVisibleGroup);
      countEl.addEventListener('keydown', e => { if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); openForVisibleGroup(); } });
    }

    if(!carousel || rowEls.length < 2){
      if(carousel && defaultIdx > 0){
        requestAnimationFrame(() => { carousel.scrollLeft = rowEls[defaultIdx] ? rowEls[defaultIdx].offsetLeft : 0; });
      }
      return;
    }
    // 각 그룹 행의 실제 위치(offsetLeft)로 정확히 스크롤한다. clientWidth*idx처럼 정수로
    // 반올림된 너비를 곱해 계산하면 그룹이 2, 3번째로 갈수록 오차가 누적되어 테두리가
    // 살짝 잘려 보이는 문제가 있었다.
    function scrollToIdx(idx, smooth){
      idx = Math.max(0, Math.min(rowEls.length - 1, idx));
      carousel.scrollTo({ left: rowEls[idx].offsetLeft, behavior: smooth === false ? 'auto' : 'smooth' });
    }
    function currentIdx(){
      let best = 0, bestDiff = Infinity;
      rowEls.forEach((row, i) => {
        const diff = Math.abs(row.offsetLeft - carousel.scrollLeft);
        if(diff < bestDiff){ bestDiff = diff; best = i; }
      });
      return best;
    }
    function syncUI(idx){
      dots.forEach((d, i) => d.classList.toggle('active', i === idx));
      if(prevBtn) prevBtn.disabled = idx === 0;
      if(nextBtn) nextBtn.disabled = idx === rowEls.length - 1;
    }
    if(defaultIdx > 0){
      requestAnimationFrame(() => scrollToIdx(defaultIdx, false));
    }
    syncUI(defaultIdx);
    dots.forEach(dot => {
      dot.addEventListener('click', () => scrollToIdx(parseInt(dot.dataset.idx, 10), true));
    });
    if(prevBtn) prevBtn.addEventListener('click', () => scrollToIdx(currentIdx() - 1, true));
    if(nextBtn) nextBtn.addEventListener('click', () => scrollToIdx(currentIdx() + 1, true));
    let scrollTimer = null;
    carousel.addEventListener('scroll', () => {
      if(scrollTimer) clearTimeout(scrollTimer);
      scrollTimer = setTimeout(() => syncUI(currentIdx()), 80);
    });
  });
})();

/* ---------------- kanban board ---------------- */
// drop 계열(drop/보류(DROP)/HOLD)은 같은 상태의 순차 전환 라벨이라 토글 하나로 함께 숨김/표시한다.
const DROP_GROUP_STATUSES = ['drop', '보류(DROP)', 'HOLD'];
const HIDEABLE_STATUSES = [...DROP_GROUP_STATUSES, '접수완료'];
let hiddenBoardStatuses = new Set(HIDEABLE_STATUSES); // 모두 기본 숨김

/* ---- 상태별 일감 보드 전용 조직 필터 (Reporter 기준, 다중 선택) ---- */
// 빈 Set = 필터 없음(전체 표시). 이 필터는 보드에만 적용되고 위쪽 "일감 현황 요약" 타일에는 영향을 주지 않는다.
const BOARD_ORGS = Array.from(new Set(DATA.tickets.map(t => t.reporterOrg).filter(Boolean)))
  .sort((a, b) => a.localeCompare(b, 'ko'));
let selectedBoardOrgs = new Set();

function boardOrgFilterLabel(){
  if(selectedBoardOrgs.size === 0) return '조직: 전체';
  if(selectedBoardOrgs.size === 1) return `조직: ${[...selectedBoardOrgs][0]}`;
  return `조직: ${selectedBoardOrgs.size}개 선택`;
}
function renderOrgFilterPanel(){
  const panel = document.getElementById('orgFilterPanel');
  panel.innerHTML = BOARD_ORGS.map(org => `
    <label class="org-filter-option">
      <input type="checkbox" value="${esc(org)}" ${selectedBoardOrgs.has(org) ? 'checked' : ''}>
      <span>${esc(org)}</span>
    </label>
  `).join('') + `
    <div class="org-filter-actions">
      <button type="button" id="orgFilterSelectAll">전체 선택</button>
      <button type="button" id="orgFilterClear">초기화</button>
    </div>
  `;
  $$('input[type="checkbox"]', panel).forEach(cb => {
    cb.addEventListener('change', () => {
      if(cb.checked) selectedBoardOrgs.add(cb.value); else selectedBoardOrgs.delete(cb.value);
      document.getElementById('orgFilterBtnLabel').textContent = boardOrgFilterLabel();
      renderBoard();
    });
  });
  document.getElementById('orgFilterSelectAll').addEventListener('click', () => {
    selectedBoardOrgs = new Set(BOARD_ORGS);
    renderOrgFilterPanel();
    document.getElementById('orgFilterBtnLabel').textContent = boardOrgFilterLabel();
    renderBoard();
  });
  document.getElementById('orgFilterClear').addEventListener('click', () => {
    selectedBoardOrgs = new Set();
    renderOrgFilterPanel();
    document.getElementById('orgFilterBtnLabel').textContent = boardOrgFilterLabel();
    renderBoard();
  });
}
renderOrgFilterPanel();
const boardOrgFilterEl = document.getElementById('boardOrgFilter');
document.getElementById('orgFilterBtn').addEventListener('click', (e) => {
  e.stopPropagation();
  boardOrgFilterEl.classList.toggle('open');
});
document.addEventListener('click', (e) => {
  if(boardOrgFilterEl.classList.contains('open') && !boardOrgFilterEl.contains(e.target)){
    boardOrgFilterEl.classList.remove('open');
  }
});
document.addEventListener('keydown', (e) => {
  if(e.key === 'Escape') boardOrgFilterEl.classList.remove('open');
});

function renderBoard(){
  const board = document.getElementById('board');
  const groups = {};
  STATUS_ORDER.forEach(s => groups[s] = []);
  const ticketsForBoard = selectedBoardOrgs.size
    ? DATA.tickets.filter(t => t.reporterOrg && selectedBoardOrgs.has(t.reporterOrg))
    : DATA.tickets;
  ticketsForBoard.forEach(t => { (groups[t.status] || (groups[t.status]=[])).push(t); });
  document.getElementById('dropCount').textContent = DROP_GROUP_STATUSES.reduce((n, s) => n + (groups[s]||[]).length, 0);
  document.getElementById('receivedCount').textContent = (groups['접수완료']||[]).length;

  board.innerHTML = STATUS_ORDER.map(status => {
    const list = groups[status] || [];
    const m = STATUS_META[status];
    const isHideable = HIDEABLE_STATUSES.includes(status);
    const isShown = !isHideable || !hiddenBoardStatuses.has(status);
    const cardsHtml = list.length ? list.map(t => `
      <div class="tcard" style="--c:var(${m.c})" data-key="${esc(t.key)}">
        <div class="summary">${esc(t.summary)}</div>
        <div class="key">${esc(t.key)}</div>
        <div class="flow"><span>${esc(t.reporterName || '-')} → ${esc(t.assigneeName || '-')}</span><span>${fmtDateShort(t.created)}</span></div>
      </div>
    `).join('') : `<div class="empty-col">해당 없음</div>`;
    return `
      <div class="board-col ${isHideable ? 'is-hideable' + (isShown?' show':'') : ''}">
        <div class="board-col-head" style="color:var(${m.c})">${m.label} <span class="cnt">${list.length}</span></div>
        <div class="board-cards">${cardsHtml}</div>
      </div>
    `;
  }).join('');

  $$('.tcard', board).forEach(el => {
    el.addEventListener('click', () => {
      const t = DATA.tickets.find(x => x.key === el.dataset.key);
      if(t) openTicketDrawer(t);
    });
  });
}
renderBoard();
function bindBoardToggle(btnId, statuses){
  const list = Array.isArray(statuses) ? statuses : [statuses];
  const btn = document.getElementById(btnId);
  const isShown = () => list.every(s => !hiddenBoardStatuses.has(s));
  btn.classList.toggle('on', isShown());
  btn.addEventListener('click', function(){
    if(isShown()) list.forEach(s => hiddenBoardStatuses.add(s));
    else list.forEach(s => hiddenBoardStatuses.delete(s));
    this.classList.toggle('on', isShown());
    renderBoard();
  });
}
bindBoardToggle('dropToggle', DROP_GROUP_STATUSES);
bindBoardToggle('receivedToggle', '접수완료');

/* ---------------- drawer ---------------- */
const drawer = document.getElementById('drawer');
const scrim = document.getElementById('scrim');
function openDrawer(){ drawer.classList.add('show'); scrim.classList.add('show'); drawer.setAttribute('aria-hidden','false'); }
function closeDrawer(){ drawer.classList.remove('show'); scrim.classList.remove('show'); drawer.setAttribute('aria-hidden','true'); }
document.getElementById('drawerClose').addEventListener('click', closeDrawer);
scrim.addEventListener('click', closeDrawer);
document.addEventListener('keydown', e => { if(e.key === 'Escape') closeDrawer(); });

function openTicketDrawer(t){
  document.getElementById('drawerKind').textContent = 'Ticket · ' + (t.type||'');
  document.getElementById('drawerTitle').innerHTML = esc(t.summary);
  document.getElementById('drawerBody').innerHTML = `
    <div>${statusBadge(t.status)}</div>
    <dl class="dl">
      <dt>Jira Key</dt><dd class="mono">${esc(t.key)}</dd>
      <dt>Reporter</dt><dd>${esc(t.reporterName||'-')}${t.reporterOrg ? ` <span class="org-tag">${esc(t.reporterOrg)}</span>` : ''}</dd>
      <dt>Assignee</dt><dd>${esc(t.assigneeName||'-')}${t.assigneeOrg ? ` <span class="org-tag">${esc(t.assigneeOrg)}</span>` : ''}</dd>
      <dt>Request Ver.</dt><dd class="mono">${esc((t.reqVersion||'').replace('B tv VCS ','') || '-')}</dd>
      <dt>Component</dt><dd>${esc(t.component||'-')}</dd>
      <dt>PoC</dt><dd>${esc(t.poc||'-')}</dd>
      <dt>등록일</dt><dd class="mono">${fmtDate(t.created)}</dd>
      <dt>업데이트</dt><dd class="mono">${fmtDate(t.updated)}</dd>
    </dl>
    ${renderHistorySection(t)}
    <hr class="dv">
    <div class="field-block">
      <div class="k">Fix Version</div>
      <div class="v na">-</div>
    </div>
    <div class="field-block">
      <div class="k">개발 배경/목적 · 주요 개발내용</div>
      <div class="v na">-</div>
    </div>
    ${t.jiraUrl ? `<a class="drawer-link" href="${esc(t.jiraUrl)}" target="_blank" rel="noopener">Jira에서 열기 ↗</a>` : ''}
  `;
  openDrawer();
}

function openMilestoneDrawer(m){
  document.getElementById('drawerKind').textContent = 'Milestone · ' + m.version;
  document.getElementById('drawerTitle').innerHTML = esc(m.name);
  const finishHtml = isInvalid(m.finish)
    ? `<dd class="mono" style="color:var(--st-review)">${esc(m.finish.raw)} ⚠ 날짜 형식 확인 필요</dd>`
    : `<dd class="mono">${fmtDate(m.finish)}</dd>`;
  document.getElementById('drawerBody').innerHTML = `
    <dl class="dl">
      <dt>Version</dt><dd class="mono">${esc(m.version)}</dd>
      <dt>시작일</dt><dd class="mono">${fmtDate(m.start)}</dd>
      <dt>종료일</dt>${finishHtml}
      <dt>Status</dt><dd>${m.status ? esc(m.status) : '<span class="v na" style="display:inline">- (지난 날짜라도 완료로 단정하지 않음)</span>'}</dd>
      <dt>Updated</dt><dd class="mono">${fmtDate(m.updated)}</dd>
    </dl>
    ${isInvalid(m.finish) ? `<div class="data-note" style="margin:0"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 9v4M12 17h.01M10.29 3.86 1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0Z"/></svg><div>원본 KB의 종료일 값이 달력에 없는 날짜(9월 31일)로 기재되어 있어 그대로 표시했습니다. 정합성 확인이 필요합니다.</div></div>` : ''}
  `;
  openDrawer();
}

function baseVersionForMatch(v){
  return String(v || '').replace(/#\d+/, '').trim();
}
function compareTicketKeyAsc(a, b){
  const ma = String(a).match(/^([A-Za-z]+)-?(\d+)$/);
  const mb = String(b).match(/^([A-Za-z]+)-?(\d+)$/);
  if(ma && mb){
    if(ma[1] !== mb[1]) return ma[1] < mb[1] ? -1 : 1;
    return parseInt(ma[2], 10) - parseInt(mb[2], 10);
  }
  return a < b ? -1 : a > b ? 1 : 0;
}
function ticketsForRelease(r){
  const target = baseVersionForMatch(r.version);
  if(!target) return [];
  return DATA.tickets.filter(t => {
    if(!t.reqVersion) return false;
    const m = t.reqVersion.match(/(\d+\.\d+(?:\.\d+)?)/);
    const v = m ? m[1] : t.reqVersion.trim();
    return v === target;
  }).slice().sort((a, b) => compareTicketKeyAsc(b.key, a.key));
}
function openReleaseDrawer(r){
  document.getElementById('drawerKind').textContent = 'Release · ' + r.version;
  document.getElementById('drawerTitle').innerHTML = esc(r.version);
  const relatedTickets = ticketsForRelease(r);
  document.getElementById('drawerBody').innerHTML = `
    <div class="field-block">
      <div class="k">대상 일감 (${relatedTickets.length}건, Jira Key 내림차순)</div>
      <div class="v ${relatedTickets.length?'':'na'}">${relatedTickets.length ? `<ul class="rel-ticket-list">${relatedTickets.map(t => `<li><a class="rt-key" href="${esc(t.jiraUrl)}" target="_blank" rel="noopener">${esc(t.key)} ↗</a><span class="rt-summary">${esc(t.summary || '-')}</span></li>`).join('')}</ul>` : 'KB에 연결된 대상 일감이 없습니다'}</div>
    </div>
  `;
  openDrawer();
}

// 상단 status 타일 클릭 시: 예전엔 아래 "전체 일감 조회" 표를 필터링해 스크롤했지만,
// 그 표가 제거되면서 버전별 배포 현황의 openReleaseDrawer와 같은 방식으로 — 클릭한
// 상태에 해당하는 일감 목록을 옆 드로어에 바로 띄우는 방식으로 대체한다.
function ticketsByStatuses(statuses){
  const rows = statuses ? DATA.tickets.filter(t => statuses.includes(t.status)) : DATA.tickets.slice();
  return rows.slice().sort((a, b) => compareTicketKeyAsc(b.key, a.key));
}
function openStatusDrawer(statuses, label){
  document.getElementById('drawerKind').textContent = 'Ticket List · ' + label;
  document.getElementById('drawerTitle').innerHTML = esc(label);
  const rows = ticketsByStatuses(statuses);
  document.getElementById('drawerBody').innerHTML = `
    <div class="field-block">
      <div class="k">대상 일감 (${rows.length}건, Jira Key 내림차순)</div>
      <div class="v ${rows.length?'':'na'}">${rows.length ? `<ul class="rel-ticket-list">${rows.map(t => `<li><a class="rt-key" href="${esc(t.jiraUrl)}" target="_blank" rel="noopener">${esc(t.key)} ↗</a><span class="rt-summary">${esc(t.summary || '-')}</span></li>`).join('')}</ul>` : '해당 상태의 일감이 없습니다'}</div>
    </div>
  `;
  openDrawer();
}

/* ---------------- 간단 문답봇 (규칙 기반 조회 — 자유 생성형 AI 아님) ---------------- */
const CB_KEY_RE = /\b([A-Za-z]{2,10}-\d{1,6})\b/;
const CB_VERSION_RE = /(5\.6\.\d+)\s*(?:#\s*(\d+))?/i;
const CB_COST_KEYWORDS = ['개발 금액','개발금액','예산','비용','금액','견적','공수','인건비'];
const CB_MILESTONE_KEYWORDS = ['마일스톤','진행단계','진행 단계','단계'];
const CB_DEPLOY_KEYWORDS = ['배포일정','배포 일정','배포일','배포 일','배포날짜','배포 날짜','배포현황','배포 현황'];
const CB_INCLUDE_KEYWORDS = ['포함','대상 일감','대상일감','일감 목록','일감목록','몇 건','몇건'];
const CB_STOPWORDS = new Set(['알려줘','알려주세요','확인','조회','좀','에서','에게','해줘','상태','진행','현황','상황','건','일감','현재','좀알려줘','줘']);
const CB_KNOWN_VERSIONS = Array.from(new Set(DATA.milestones.map(m => m.version))).sort(compareVersionDesc);

function cbFindTicket(key){
  const norm = key.toUpperCase();
  return DATA.tickets.find(t => t.key.toUpperCase() === norm);
}

function cbSharedValue(rows, field){
  const vals = new Set(rows.map(r => r[field] ?? null));
  return vals.size === 1 ? rows[0][field] : null;
}

function cbTicketAnswer(t){
  const meta = STATUS_META[t.status];
  const statusLabel = meta ? meta.label : (t.status || '-');
  const lines = [];
  lines.push(`<div class="cb-line"><b>${esc(t.key)}</b> · ${esc(t.summary || '-')}</div>`);
  lines.push(`<div class="cb-line">현재 상태: <b>${esc(statusLabel)}</b></div>`);
  if(t.statusFromHistory){
    lines.push(`<div class="cb-line">⚠ KB 로데이터 상태는 <b>${esc(STATUS_META[t.masterStatus]?.label || t.masterStatus)}</b>이지만, 히스토리 상 최종 상태를 기준으로 표시했습니다.</div>`);
  }
  lines.push(`<div class="cb-line">담당: ${esc(t.reporterName||'-')}${t.reporterOrg?` (${esc(t.reporterOrg)})`:''} → ${esc(t.assigneeName||'-')}${t.assigneeOrg?` (${esc(t.assigneeOrg)})`:''}</div>`);
  lines.push(`<div class="cb-line">Request Ver.: ${esc(t.reqVersion || '-')} · 업데이트: ${fmtDate(t.updated)}</div>`);
  lines.push(`<div class="cb-line"><button type="button" class="cb-key-link" data-key="${esc(t.key)}">일감 상세 보기 →</button></div>`);
  return lines.join('');
}

function cbVersionSummaryAnswer(lane){
  const relRows = releasesForLaneVersion(lane);
  const stage = releaseCompletionInfo(lane) || stageInfoFor(lane);
  const lines = [];
  lines.push(`<div class="cb-line"><b>${esc(lane)}</b> 현황</div>`);
  lines.push(`<div class="cb-line">${stage.badge} ${esc(stage.headline||'')}${stage.sub?` · ${esc(stage.sub)}`:''}</div>`);
  if(relRows.length){
    const sharedCount = cbSharedValue(relRows, 'ticketCount');
    lines.push(`<div class="cb-line">배포 그룹 ${relRows.length}개${sharedCount!=null?` · 대상 일감 ${sharedCount}건`:''}</div>`);
    lines.push(`<div class="cb-list">${relRows.map(r => `<div class="cb-list-item">${esc(r.group)} · <b>${esc(r.status||'-')}</b> · ${fmtDate(r.dueDate)}${r.devices?` · ${esc(r.devices)}`:''}</div>`).join('')}</div>`);
  } else {
    lines.push(`<div class="cb-line">KB에 등록된 배포 그룹 정보가 없습니다.</div>`);
  }
  return lines.join('');
}

function cbDeployScheduleAnswer(lane){
  const relRows = releasesForLaneVersion(lane);
  if(!relRows.length) return `<div class="cb-line"><b>${esc(lane)}</b>의 배포일정 정보를 KB에서 찾을 수 없습니다.</div>`;
  const sorted = relRows.slice().sort((a,b) => { const da=parseDate(a.dueDate), db=parseDate(b.dueDate); if(da&&db) return da-db; return 0; });
  const lines = [`<div class="cb-line"><b>${esc(lane)}</b> 배포일정</div>`];
  lines.push(`<div class="cb-list">${sorted.map(r => {
    const d = parseDate(r.dueDate);
    const label = (d && d < TODAY) ? '배포시작일' : '배포예정일';
    return `<div class="cb-list-item">${esc(r.group)} · ${label} <b>${fmtDate(r.dueDate)}</b> · ${esc(r.status||'-')}</div>`;
  }).join('')}</div>`);
  return lines.join('');
}

function cbIncludedTicketsAnswer(lane){
  const relRows = releasesForLaneVersion(lane);
  if(!relRows.length) return `<div class="cb-line"><b>${esc(lane)}</b>에 연결된 대상 일감 정보를 KB에서 찾을 수 없습니다.</div>`;
  const sharedCount = cbSharedValue(relRows, 'ticketCount');
  const sharedSummary = cbSharedValue(relRows, 'summary');
  const lines = [`<div class="cb-line"><b>${esc(lane)}</b> 대상 일감${sharedCount!=null?` ${sharedCount}건`:''}</div>`];
  if(sharedSummary) lines.push(`<div class="cb-line">주요 개발 내용: ${esc(sharedSummary)}</div>`);
  if(sharedCount==null){
    lines.push(`<div class="cb-list">${relRows.map(r => `<div class="cb-list-item">${esc(r.group)} · 대상 일감 ${r.ticketCount ?? '-'}건</div>`).join('')}</div>`);
  }
  lines.push(`<div class="cb-line">그룹별 상세는 "버전별 배포 현황" 섹션에서 확인하실 수 있어요.</div>`);
  return lines.join('');
}

function cbMilestoneAllAnswer(){
  const lines = [`<div class="cb-line">버전별 현재 단계</div>`];
  lines.push(`<div class="cb-list">${CB_KNOWN_VERSIONS.map(v => {
    const info = releaseCompletionInfo(v) || stageInfoFor(v);
    return `<div class="cb-list-item"><b>${esc(v)}</b> · ${info.badge} ${esc(info.headline||'')}</div>`;
  }).join('')}</div>`);
  return lines.join('');
}

function cbDeployAllAnswer(){
  const allRows = DATA.releases.slice().sort((a,b) => {
    const da = parseDate(a.dueDate), db = parseDate(b.dueDate);
    if(da && db) return da - db;
    return 0;
  });
  const lines = [`<div class="cb-line">전체 배포일정 (날짜순)</div>`];
  lines.push(`<div class="cb-list">${allRows.map(r => {
    const d = parseDate(r.dueDate);
    const label = (d && d < TODAY) ? '배포시작일' : '배포예정일';
    return `<div class="cb-list-item"><b>${esc(r.version)}</b> ${esc(r.group)} · ${label} ${fmtDate(r.dueDate)} · ${esc(r.status||'-')}</div>`;
  }).join('')}</div>`);
  return lines.join('');
}

function cbCostAnswer(){
  return `<div class="cb-line">개발 금액·예산·공수 정보는 업로드된 KB에 포함되어 있지 않아 답변드릴 수 없어요.</div>
    <div class="cb-line">해당 정보가 필요하시면 KB에 관련 항목을 추가해 다시 업로드해 주세요.</div>`;
}

function cbKeywordSearch(query){
  const trimmed = query.trim();
  if(trimmed.length < 2) return [];
  const lower = trimmed.toLowerCase();
  let matches = DATA.tickets.filter(t => t.summary && t.summary.toLowerCase().includes(lower));
  if(!matches.length){
    const tokens = trimmed.split(/\s+/).filter(s => s.length >= 2 && !CB_STOPWORDS.has(s));
    if(tokens.length){
      matches = DATA.tickets.filter(t => t.summary && tokens.some(tok => t.summary.toLowerCase().includes(tok.toLowerCase())));
    }
  }
  return matches.slice(0, 5);
}

function cbFallbackAnswer(){
  return `<div class="cb-line">죄송해요, 이해하지 못했어요. 아래처럼 물어봐 주세요.</div>
    <div class="cb-line">· Jira Key (예: BTVB-3258 진행상황)</div>
    <div class="cb-line">· 버전 (예: 5.6.2 배포일정, 5.6.2 진행현황)</div>
    <div class="cb-line">· 일감 요약 키워드 (예: GNB 메뉴 개편)</div>`;
}

function cbKeywordSearchAnswer(query){
  const matches = cbKeywordSearch(query);
  if(!matches.length) return cbFallbackAnswer();
  const lines = [`<div class="cb-line">"${esc(query)}"와 관련된 일감 ${matches.length}건${matches.length===5?' (상위 5건)':''}</div>`];
  lines.push(`<div class="cb-list">${matches.map(t => {
    const meta = STATUS_META[t.status];
    return `<div class="cb-list-item"><button type="button" class="cb-key-link" data-key="${esc(t.key)}">${esc(t.key)}</button> · ${esc(meta?meta.label:t.status)} · ${esc(t.summary)}</div>`;
  }).join('')}</div>`);
  return lines.join('');
}

function cbAnswer(query){
  const raw = query.trim();
  if(!raw) return cbFallbackAnswer();

  if(CB_COST_KEYWORDS.some(k => raw.includes(k))) return cbCostAnswer();

  const keyMatch = raw.match(CB_KEY_RE);
  if(keyMatch){
    const t = cbFindTicket(keyMatch[1]);
    if(t) return cbTicketAnswer(t);
    return `<div class="cb-line">Jira Key <b>${esc(keyMatch[1].toUpperCase())}</b>를 KB에서 찾을 수 없습니다.</div>`;
  }

  const verMatch = raw.match(CB_VERSION_RE);
  if(verMatch){
    const lane = verMatch[2] ? `${verMatch[1]} #${verMatch[2]}` : verMatch[1];
    if(!CB_KNOWN_VERSIONS.includes(lane)){
      return `<div class="cb-line">버전 <b>${esc(lane)}</b> 정보를 KB에서 찾을 수 없습니다. (등록된 버전: ${CB_KNOWN_VERSIONS.map(v=>esc(v)).join(', ')})</div>`;
    }
    if(CB_MILESTONE_KEYWORDS.some(k => raw.includes(k))){
      const info = releaseCompletionInfo(lane) || stageInfoFor(lane);
      return `<div class="cb-line"><b>${esc(lane)}</b> 마일스톤 현황</div><div class="cb-line">${info.badge} ${esc(info.headline||'')}${info.sub?` · ${esc(info.sub)}`:''}</div>`;
    }
    if(CB_DEPLOY_KEYWORDS.some(k => raw.includes(k))) return cbDeployScheduleAnswer(lane);
    if(CB_INCLUDE_KEYWORDS.some(k => raw.includes(k))) return cbIncludedTicketsAnswer(lane);
    return cbVersionSummaryAnswer(lane);
  }

  if(CB_MILESTONE_KEYWORDS.some(k => raw.includes(k))) return cbMilestoneAllAnswer();
  if(CB_DEPLOY_KEYWORDS.some(k => raw.includes(k))) return cbDeployAllAnswer();

  return cbKeywordSearchAnswer(raw);
}

(function initChatbot(){
  const fab = document.getElementById('chatbotFab');
  const panel = document.getElementById('chatbotPanel');
  const closeBtn = document.getElementById('chatbotClose');
  const messagesWrap = document.getElementById('chatbotMessages');
  const chipsWrap = document.getElementById('chatbotChips');
  const form = document.getElementById('chatbotForm');
  const input = document.getElementById('chatbotInput');
  if(!fab || !panel) return;

  const SUGGESTIONS = ['5.6.2 배포일정', '5.6.2 진행현황', 'BTVB-3258 진행상황'];

  function addMessage(role, html){
    const row = document.createElement('div');
    row.className = 'cb-msg ' + role;
    const bubble = document.createElement('div');
    bubble.className = 'cb-bubble';
    bubble.innerHTML = html;
    row.appendChild(bubble);
    messagesWrap.appendChild(row);
    messagesWrap.scrollTop = messagesWrap.scrollHeight;
    bubble.querySelectorAll('.cb-key-link').forEach(btn => {
      btn.addEventListener('click', () => {
        const t = DATA.tickets.find(x => x.key === btn.dataset.key);
        if(t) openTicketDrawer(t);
      });
    });
  }

  function handleQuery(text){
    addMessage('user', esc(text));
    addMessage('bot', cbAnswer(text));
  }

  function renderChips(){
    chipsWrap.innerHTML = SUGGESTIONS.map(s => `<button type="button" class="chatbot-chip">${esc(s)}</button>`).join('');
    chipsWrap.querySelectorAll('.chatbot-chip').forEach(chip => {
      chip.addEventListener('click', () => handleQuery(chip.textContent));
    });
  }

  let initialized = false;
  function openPanel(){
    panel.hidden = false;
    fab.classList.add('is-open');
    if(!initialized){
      addMessage('bot', `<div class="cb-line">안녕하세요! 업로드된 KB 데이터를 기준으로 일감 진행 현황, 버전별 대상 일감, 배포일정, 마일스톤을 조회해드려요.</div><div class="cb-line">자유 대화형 AI가 아니라 정해진 항목만 규칙적으로 조회하는 방식이에요.</div>`);
      renderChips();
      initialized = true;
    }
    input.focus();
  }
  function closePanel(){
    panel.hidden = true;
    fab.classList.remove('is-open');
  }

  fab.addEventListener('click', () => {
    if(panel.hidden) openPanel(); else closePanel();
  });
  closeBtn.addEventListener('click', closePanel);

  form.addEventListener('submit', (ev) => {
    ev.preventDefault();
    const text = input.value.trim();
    if(!text) return;
    handleQuery(text);
    input.value = '';
  });
})();

</script>

</body>
</html>

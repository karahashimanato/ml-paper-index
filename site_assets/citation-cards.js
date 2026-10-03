// 記事中の引用 [card-id#c1] にカーソルを当てる(スマホではタップする)と、論文名・場所・主張・原文の引用をカードで表示する。
// データは scripts/build_site.py が各記事の末尾に埋め込む <script id="citation-data"> の JSON。
(function () {
  "use strict";
  var CITE = /^((?:arxiv|doi|exp)-[^#\s]+)#([cr][0-9]+)$/;
  var data = null;
  var card = null;
  var current = null;
  var hideTimer = null;

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  function build(key) {
    var d = data[key];
    var root = el("div", "cite-card__body");
    var head = el("div", "cite-card__title");
    if (d.card) {
      var a = el("a", null, d.title);
      a.href = d.card;
      head.appendChild(a);
    } else {
      head.textContent = d.title;
    }
    root.appendChild(head);
    var meta = [d.authors, d.year, d.version].filter(Boolean).join(" · ");
    if (meta) root.appendChild(el("div", "cite-card__meta", meta));
    var where = [d.location, d.page ? "p." + d.page : ""].filter(Boolean).join(", ");
    if (where) root.appendChild(el("div", "cite-card__where", where));
    if (d.summary) root.appendChild(el("div", "cite-card__summary", d.summary));
    if (d.quote) {
      var q = el("blockquote", "cite-card__quote");
      q.appendChild(el("span", "cite-card__quote-label", "原文"));
      q.appendChild(document.createTextNode(d.quote));
      root.appendChild(q);
    }
    var foot = el("div", "cite-card__foot");
    foot.appendChild(el("span", "cite-card__id", key));
    if (d.url) {
      var open = el("a", "cite-card__open", d.page ? "PDF の p." + d.page + " を開く" : "出典を開く");
      open.href = d.url;
      open.target = "_blank";
      open.rel = "noopener";
      foot.appendChild(open);
    }
    root.appendChild(foot);
    return root;
  }

  function place(link) {
    var r = link.getBoundingClientRect();
    var w = card.offsetWidth, h = card.offsetHeight;
    var vw = document.documentElement.clientWidth, vh = window.innerHeight;
    var left = Math.min(Math.max(8, r.left), vw - w - 8);
    var below = r.bottom + 8;
    var top = (below + h > vh - 8 && r.top - h - 8 > 8) ? r.top - h - 8 : below;
    card.style.left = left + window.scrollX + "px";
    card.style.top = top + window.scrollY + "px";
  }

  function show(link) {
    clearTimeout(hideTimer);
    if (current === link && card.classList.contains("is-open")) return;
    current = link;
    card.replaceChildren(build(link.dataset.cite));
    card.classList.add("is-open");
    card.setAttribute("aria-hidden", "false");
    place(link);
  }

  function hide(delay) {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(function () {
      card.classList.remove("is-open");
      card.setAttribute("aria-hidden", "true");
      current = null;
    }, delay || 0);
  }

  function init() {
    var node = document.getElementById("citation-data");
    if (!node) return;
    try { data = JSON.parse(node.textContent); } catch (e) { return; }
    card = el("div", "cite-card");
    card.setAttribute("role", "tooltip");
    card.setAttribute("aria-hidden", "true");
    document.body.appendChild(card);
    card.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
    card.addEventListener("mouseleave", function () { hide(150); });

    var links = document.querySelectorAll(".md-content a");
    links.forEach(function (link) {
      var m = CITE.exec(link.textContent.trim());
      if (!m || !data[m[0]]) return;
      link.dataset.cite = m[0];
      link.classList.add("cite-link");
      link.removeAttribute("title");
      link.addEventListener("mouseenter", function () { show(link); });
      link.addEventListener("mouseleave", function () { hide(200); });
      link.addEventListener("focus", function () { show(link); });
      link.addEventListener("blur", function () { hide(200); });
      // タッチ端末では1回目のタップでカードを開き、カード内のリンクから PDF を開く
      link.addEventListener("click", function (e) {
        if (window.matchMedia("(hover: none)").matches && current !== link) {
          e.preventDefault();
          show(link);
        }
      });
    });
    document.addEventListener("click", function (e) {
      if (card.classList.contains("is-open") && !card.contains(e.target) && !(e.target.closest && e.target.closest(".cite-link"))) hide(0);
    });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") hide(0); });
    window.addEventListener("resize", function () { if (current) place(current); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();

const header = document.querySelector('#site-header');
const hero = document.querySelector('#hero');
function updateHeader() {
  if (!hero) return;
  header.classList.toggle('compact', window.scrollY > 30);
  header.classList.toggle('past-hero', hero.getBoundingClientRect().bottom <= 0);
}
window.addEventListener('scroll', updateHeader, { passive: true });
window.addEventListener('resize', updateHeader);
updateHeader();
const moreButton = document.querySelector('.more-toggle');
const moreLinks = document.querySelector('#more-links');
function closeMore() { moreButton.setAttribute('aria-expanded', 'false'); moreLinks.hidden = true; }
moreButton.addEventListener('click', () => {
  const opening = moreLinks.hidden;
  moreLinks.hidden = !opening;
  moreButton.setAttribute('aria-expanded', String(opening));
});
document.addEventListener('click', event => { if (!event.target.closest('.more-wrap')) closeMore(); });
const navButton = document.querySelector('.nav-toggle');
const nav = document.querySelector('#navigation');
navButton.addEventListener('click', () => {
  const opening = nav.classList.toggle('is-open');
  navButton.setAttribute('aria-expanded', String(opening));
});
document.addEventListener('keydown', event => {
  if (event.key !== 'Escape') return;
  if (!moreLinks.hidden) { closeMore(); moreButton.focus(); }
  else if (nav.classList.contains('is-open')) { nav.classList.remove('is-open'); navButton.setAttribute('aria-expanded', 'false'); navButton.focus(); }
});

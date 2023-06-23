function hideDiv() {
  document.getElementById("content_div").style.display = "none";
  document.getElementById("loader_div").style.display = "flex";
}
window.onload = function () {
  console.log("Load window");
  try {
    var downloadLink = document.getElementById("csv_link");
    downloadLink.click();
  } catch (error) {}
};
let currentPage = 1;
const form = document.getElementById('createEventForm');

function showPage(pageNumber) {
  const pages = document.getElementsByClassName('page');
  for (let i = 0; i < pages.length; i++) {
    if (i + 1 === pageNumber) {
      pages[i].classList.add('active');
    } else {
      pages[i].classList.remove('active');
    }
  }
}

function nextPage() {
  currentPage++;
  showPage(currentPage);
}

function previousPage() {
  currentPage--;
  showPage(currentPage);
}

showPage(currentPage);

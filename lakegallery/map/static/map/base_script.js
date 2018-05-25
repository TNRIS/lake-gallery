//variables
var input, filter, lakeMenu, atags, atagsLength, myArray, i;
//function to search and filter lakes
function lakeSearch() {
  input = document.getElementById("search");
  filter = input.value.toUpperCase();
  lakeMenu = document.getElementById("lakeMenu");
  items = lakeMenu.getElementsByClassName("dropdown-item");
  menuItemsLength = items.length;
  checkArray = [];
  // Loop through all enabled lake items, and hide those who don't match the search query
  for (i = 0; i < menuItemsLength; i++) {
    var item = items[i];
    if (item) {
      if (item.innerHTML.toUpperCase().indexOf(filter) > -1) {
        item.style.display = "";
        document.getElementById("noneAvailable").style.display = "none";
      }
      else {
        item.style.display = "none";
        checkArray.push(item);
        if (checkArray.length == menuItemsLength) {
          document.getElementById("noneAvailable").style.display = "block";
        }
      }
    }
  }
};
//function to clear search text onclick
function clearSearch() {
  document.getElementById("theForm").reset();
  lakeSearch();
};

function showMenuPanel(panelID) {
  const menuLevel1 = document.getElementById(panelID);
  const button = document.getElementById("menu-button");
  if (menuLevel1.classList.contains("not-shown")) {
    button.classList.add("active");
    menuLevel1.classList.remove("not-shown");
  } else {
    menuLevel1.classList.add("not-shown");
    button.classList.remove("active");
  }
}

document.querySelector(".contact").addEventListener("click", showInfo());

function showInfo() {
  let me = document.querySelector(".me");
  const name = document.createElement("p");
  name.innerText = "mee is stupid!";
  document.body.contact.appendChild(me);
  console.log("HEllo");
}

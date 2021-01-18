const firstName = document.getElementById("firstName");
const lastName = document.getElementById("lastName");
const email = document.getElementById("email");
const phone = document.getElementById("phone");
const zip = document.getElementById("zip");

firstName.addEventListener("blur", validateFN);
lastName.addEventListener("blur", validateLN);
email.addEventListener("blur", validateEmail);
phone.addEventListener("blur", validatePhone);
zip.addEventListener("blur", validateZip);

function validateFN() {
  const re = /^[a-zA-Z]{2,8}$/;
  if (!re.test(firstName.value)) {
    firstName.classList.add("is-invalid");
    firstName.classList.remove("is-valid");
  } else {
    firstName.classList.add("is-valid");
    firstName.classList.remove("is-invalid");
  }
}

function validateLN() {
  const re = /^[a-zA-Z]{2,8}$/;
  if (!re.test(lastName.value)) {
    lastName.classList.add("is-invalid");
    lastName.classList.remove("is-valid");
  } else {
    lastName.classList.add("is-valid");
    lastName.classList.remove("is-invalid");
  }
}

function validateEmail() {
  const re = /^([a-zA-Z0-9_\.\-]+)@([a-zA-Z0-9_\.\-]+)\.[a-zA-Z]{2,5}$/;
  if (!re.test(email.value)) {
    email.classList.add("is-invalid");
    email.classList.remove("is-valid");
  } else {
    email.classList.add("is-valid");
    email.classList.remove("is-invalid");
  }
}

// (333).444.5555
// 333-444-5555
// 3334445555

function validatePhone() {
  const re = /^\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}$/;
  if (!re.test(phone.value)) {
    phone.classList.add("is-invalid");
    phone.classList.remove("is-valid");
  } else {
    phone.classList.add("is-valid");
    phone.classList.remove("is-invalid");
  }
}

function validateZip() {
  const re = /^[0-9]{5}(-[0-9])?$/;
  if (!re.test(zip.value)) {
    zip.classList.add("is-invalid");
    zip.classList.remove("is-valid");
  } else {
    zip.classList.add("is-valid");
    zip.classList.remove("is-invalid");
  }
}

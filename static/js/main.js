
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
} 



document.addEventListener("DOMContentLoaded", function() {
  var popup = document.getElementById("popup");

  // Mostrar el pop-up solo si no se ha marcado el checkbox de la edad
  if (!localStorage.getItem("ageConfirmed")) {
      popup.style.display = "block";
  }
});

function closePopup() {
  var ageCheckbox = document.getElementById("age-checkbox");
  var termsCheckbox = document.getElementById("terms-checkbox");

  // Verificar si ambos checkboxes están marcados
  if (ageCheckbox.checked && termsCheckbox.checked) {
      localStorage.setItem("ageConfirmed", "true");
      document.getElementById("popup").style.display = "none";
  } else {
      alert("Por favor, confirma que tienes al menos 18 años y que has leído nuestros términos y condiciones.");
  }
}

function toggleHighlights(name) 
{
  const s=`.${name}`;
  const c=document.getElementById(`highlights-content-${name}`);
  document.querySelector(s).style.color="rgb(238, 75, 43)";
  if(c.style.display==="none" || c.style.display==="")
  {
    c.style.display="block";
  }
  else
  {
    c.style.display="none";
    document.querySelector(s).style.color="white";
  }
}
document.addEventListener('DOMContentLoaded', function () {
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');

  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function () {
      const row = this.closest('tr');
      if (this.checked) {
        row.style.backgroundColor = 'green'; 
  
      } else {
        row.style.backgroundColor = '';  
      }
    });
  });
});

fetch("https://pokeapi.co/api/v2/pokemon/pokemon")
  .then(response=>response.json())
  .then(data=>console.log(data.id))
  .catch(error=>console.error(error));

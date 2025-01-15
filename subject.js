function open(subject) 
{
  console.log(subject);
   alert("You selected the subject course");
  if (subject === 'wt') {
      window.location.href = 'wt.htmlasync function fetchTopics() {
    const response = await fetch('topics'); 
    const topics = await response.json();

    const unitContainer = document.querySelector('.syllabus');

    topics.forEach(topic => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><input type="checkbox"></td>
            <td>${topic.title}</td>
            <td><a href="${topic.article_url}" target="_blank"><img src="images/gfg.png" alt="GeeksforGeeks"></a></td>
            <td><a href="${topic.youtube_url}" target="_blank"><img src="images/youtube.png" alt="YouTube"></a></td>
            <td>${topic.revision}</td>
        `;
        unitContainer.appendChild(row);
    });
}



const section_ids = ['about', 'contact', 'education', 'projects', 'work-experience']
const sections = document.querySelectorAll('.page-section');
const links = document.querySelectorAll('.nav-link');


links.forEach(link => {
    link.addEventListener('click', e => {
        goToSection(e)
    })
})



const goToSection = e => {
    const newDestination = document.querySelector(e.currentTarget.getAttribute('href'))
    console.log(newDestination);
    sections.forEach(section => {
        section.classList.add('hide-section')
    })
    newDestination.classList.remove('hide-section')
}
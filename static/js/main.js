

 
let searchForm = document.getElementById("searchForm")
let pageLink = document.getElementsByClassName("page-link")
if(searchForm){
    for(let i=0;pageLink.length > i;i++)
    {
        pageLink[i].addEventListener('click',(e)=>{
            e.preventDefault()
            let page = e.currentTarget.dataset.page
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            // name  and value are a pair which menas that when a submit happens the id and value are passed as name = value
            searchForm.submit()
        })
    }
}
 

let tags = document.getElementsByClassName('project-tag')

for (let i = 0; tags.length > i; i++) {
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        // console.log('TAG ID:', tagId)
        // console.log('PROJECT ID:', projectId)

        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })

    })
}

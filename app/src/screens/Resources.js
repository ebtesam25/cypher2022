import { useState } from 'react';
import Navbar from '../components/NavBar';
import data from '../utils/data.json'

export default function Resources() {
    const [id, setid] = useState(0)
    const [search, setsearch] = useState('')
  return (
    <div className="App">
      <Navbar/>
        <input type="checkbox" id="details" class="modal-toggle"/>
        <label for="details" class="modal cursor-pointer">
        <label class="modal-box relative" for="">
        <h3 class="font-bold text-lg">{data[id]['name of resource']}</h3>
                    <span class="badge badge-primary badge-sm">{data[id].category}</span>
                    <p className="pt-2 font-medium font-xs">Description:</p>
                    <p className="font-light">{data[id].description}</p>
                    <p className="pt-2 font-medium font-xs">Eligibility:</p>
                    <p className="font-light">{data[id].eligibility}</p>
                    <p className="pt-2 font-medium font-xs">Contact:</p>
                    <p className="font-light">{data[id].contactInfo}</p>
                    <p className="pt-2 font-medium font-xs">Tags:</p>
                    <div className="font-bold badge badge-ghost badge-sm">{data[id].tags}</div>
                    <div className="mt-4">
                    <a href={data[id].link}><button class="btn btn-primary mr-4 float-left">Website</button></a>
                    {data[id].Coordinates!="Online"&&<a href={`http://www.google.com/maps/place/${data[id].Coordinates}`}><button class={`btn btn-secondary mr-4 float-right`}>Map</button></a>}
                    
                    </div>
        </label>
        </label>
    <body>
    <div class="form-control p-4 w-screen">
  <div class="input-group">
    <input type="text" placeholder="Search…" value={search} onChange={(e)=>setsearch(e.target.value)} class="input input-bordered"/>
    <button class="btn btn-square">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
    </button>
  </div>
</div>
      <div class="overflow-x-auto">
  <table class="table w-full">
    <thead className="bg-secondary">
      <tr>
        <th></th>
        <th>Name</th>
        <th>Eligibility</th>
        <th>Tags</th>
      </tr>
    </thead>
    <tbody>
      {data.map((item)=>((item.tags.includes(search) || item.description.includes(search) || item.category.includes(search) || item['name of resource'].includes(search))&&<tr>
        <th>{item.id+1}</th>
        <td><div onClick={()=>setid(parseInt(item.id))}>
            <label for="details" class="btn-ghost">{item['name of resource']}</label>
            </div><span class="badge badge-ghost badge-sm">{item.category}</span></td>
        <td>{item.eligibility}</td>
        <td><span class="badge badge-ghost badge-sm">{item.tags}</span></td>
      </tr>))}
    </tbody>
  </table>
</div>
</body>

      
      
    </div>
  );
}

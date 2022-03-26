import { useState } from 'react';
import Navbar from '../components/NavBar';
import data from '../utils/data.json'

export default function Resources() {
    const [id, setid] = useState(0)
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
                    <p className="pt-2 font-medium font-xs">Tags:</p>
                    <div className="font-bold badge badge-ghost badge-sm">{data[id].tags}</div>
                    <div className="mt-4">
                    <a href={data[id].link}><button class="btn btn-primary mr-4 float-left">Website</button></a>
                    <a href={data[id].contactInfo}><button class="btn btn-secondary mr-4 float-right">Contact</button></a>
                    </div>
        </label>
        </label>
    <body>
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
      {data.map((item)=>(<tr>
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

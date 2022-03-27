import { Link } from 'react-router-dom';

export default function Home(){
    return(
        <div class="hero min-h-screen bg-gradient-to-b from-primary via-yellow-200 to-secondary">
        <div class="hero-content flex-col lg:flex-row">
            <img src="https://cdn.discordapp.com/attachments/709603404673974273/957335638909259796/image.png" class="max-w-sm" />
            <div>
            <h1 class="text-5xl font-bold text-primary">Welcome to Immigrace!</h1>
            <p class="py-6"> ImmiGrace is a curated and scalable list of resources for immigrants of all kinds with its own search engine. On top of its own search engine, ImmiGrace includes an interactive SMS chatbot that helps its users to receive guidance, and query ImmiGrace's vast list of resources. </p>
            <Link to="/login"><button class="btn btn-primary">Get Started</button></Link>
            </div>
        </div>
        </div>
    )
}
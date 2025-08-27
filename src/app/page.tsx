'use client'
import Image from "next/image";
import {useRouter} from 'next/navigation'

import Main from './components/Main/page'

export default function Home() {

   const router = useRouter()
  function click(){

    router.push("/components/MainShop")

  }


  const hauteurVisible = window.innerHeight;


  return (

    <div className ="app-container w-[100vw] " style={{ height: `${hauteurVisible}px` }}>

      <Main />
     

    </div>



    )
}

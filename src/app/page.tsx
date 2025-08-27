'use client'
import Image from "next/image";
import {useRouter} from 'next/navigation'

import Main from './components/Main/page'

export default function Home() {

   const router = useRouter()
  function click(){

    router.push("/components/MainShop")

  }


  return (

    <div className ="app-container h-[100vh] w-[100vw] ">

      <Main />
     

    </div>



    )
}

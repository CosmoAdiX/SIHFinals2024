import { Float, Html, Loader, MeshTransmissionMaterial, Scroll, ScrollControls, Sparkles, Stars, Text } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";
import { Suspense, useState } from "react";
import { ExperienceV1 } from "../Components/ExperienceV1";
import { Iphone } from "../Components/IphoneLog";
import { Navbar } from "../Components/NavBar";
import { EthereumLogo } from "../Components/EthLogo";
import { Bloom, EffectComposer } from "@react-three/postprocessing";
import Airnt from "./assets/fonts/Airnt.otf"

function App() {
  return (
    <div className="main w-full">
      <div className="hero w-full h-screen">
        <Canvas shadows camera={{ position: [0, 0, 5], fov: 50 }}>
          <color attach="background" args={["#ef745c"]} />
          {/* <Stars radius={40} factor={2} depth={50}speed={2} /> */}
          <Sparkles count={500} size={2} scale={9} color="#fff0f3" />
          <Suspense>
            <ExperienceV1 />
            <Text anchorX='center' letterSpacing={0.07} maxWidth={2} anchorY='middle' position={[-2.2,0,-1]} castShadow receiveShadow font={Airnt}>
              Team CodeMon
              
              <MeshTransmissionMaterial transmission={0.8889} />
            </Text>
            
            {/* <mesh castShadow rotation={[1,1,1]}>
              <boxGeometry />
              <meshStandardMaterial metalness={0.8} roughness={0.4} />
            </mesh> */}
            <Float speed={4} rotationIntensity={1} floatIntensity={1}>
              <EthereumLogo position={[2.8,0,0]} />
            </Float>
            <ScrollControls pages={3} damping={1.2}>
              <Scroll>
                <Float speed={2.5} floatIntensity={2}>
                  <Iphone scale={0.02} />
                </Float>
              </Scroll>
            </ScrollControls>
            <EffectComposer>
              <Bloom mipmapBlur luminanceThreshold={1} radius={0.45} />
            </EffectComposer>
          </Suspense>
          
        </Canvas>
        <Loader />
      </div>
      <div className="2nd w-full h-screen">

      </div>
    </div>
  )
}

export default App;


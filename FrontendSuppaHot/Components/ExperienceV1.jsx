import { OrbitControls, SoftShadows, Environment } from "@react-three/drei"

export const ExperienceV1 = () => {
    return (
        <>
            {/* <OrbitControls /> */}
            <SoftShadows size={10} focus={0.8} samples={15} />
            <Environment preset="city" blur={0.1} />
            <directionalLight
                position={[15, 15, 15]}
                intensity={20}
                castShadow
                shadow-mapSize-width={512}
                shadow-mapSize-height={512}
                shadow-bias={-0.0001}
                shadow-camera-far={300}
                shadow-camera-left={-40}
                shadow-camera-right={40}
                shadow-camera-top={10}
                shadow-camera-bottom={-10}
                shadow-camera-near={0.1}
            />
            <ambientLight intensity={100} />
        </>
    )
}
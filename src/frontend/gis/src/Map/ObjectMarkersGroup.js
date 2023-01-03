import React, {useEffect, useState} from 'react';
import {LayerGroup, useMap} from 'react-leaflet';
import {ObjectMarker} from "./ObjectMarker";
import axios from "axios";

let markers = []

function ObjectMarkersGroup() {
    // TODO: PASSAR BOUNDS POR PARAMETRO PARA DEPOIS FAZER A QUERY
    axios.get(`${process.env.REACT_APP_API_GIS_URL}/api/markers/`).then((response) => {
        console.log(response.data)
        markers = response.data["Markers"]
    }).catch((error) => {
        console.log(error)
    })
    const map = useMap();
    const [geom, setGeom] = useState([...markers]);
    const [bounds, setBounds] = useState(map.getBounds());

    useEffect(() => {
        const cb = () => {
            setBounds(map.getBounds());
        }
        map.on('moveend', cb);

        return () => {
            map.off('moveend', cb);
        }
    }, []);

    useEffect(() => {
        console.log(`> getting data for bounds`, bounds);
        setGeom(markers);
    }, [bounds])

    return (
        <LayerGroup>
            {
                geom.map(geoJSON => <ObjectMarker key={geoJSON.properties.id} geoJSON={geoJSON}/>)
            }
        </LayerGroup>
    );
}

export default ObjectMarkersGroup;

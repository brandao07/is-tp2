import React, {useEffect, useState} from 'react';
import {LayerGroup, useMap} from 'react-leaflet';
import {ObjectMarker} from "./ObjectMarker";
import axios from "axios";

let markers = []

function ObjectMarkersGroup() {
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
        axios.get(`${process.env.REACT_APP_API_GIS_URL}/api/markers?ne_lat=${bounds._northEast.lat}&ne_lon=${bounds._northEast.lng}&sw_lat=${bounds._southWest.lat}&sw_lon=${bounds._southWest.lng}`)
            .then((response) => {
                console.log(response.data)
                markers = response.data["Markers"]
                setGeom(markers)
            }).catch((error) => {
            console.log(error)
        })
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

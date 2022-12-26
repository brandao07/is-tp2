import {Avatar, List, ListItem, ListItemIcon, ListItemText} from "@mui/material";
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import React from "react";
import {Marker, Popup} from 'react-leaflet';
import {icon as leafletIcon, point} from "leaflet";

const LIST_PROPERTIES = [
    {"key": "artist", label: "Artist", Icon: AccountCircleIcon},
    {"key": "date", label: "Date", Icon: CalendarMonthIcon},
    {"key": "rank", label: "Rank", Icon: EmojiEventsIcon},
    {"key": "streams", label: "Streams", Icon: TrendingUpIcon},
];

export function ObjectMarker({geoJSON}) {
    const properties = geoJSON?.properties
    const {id, title} = properties;
    const coordinates = geoJSON?.geometry?.coordinates;

    return (
        <Marker
            position={coordinates}
            icon={leafletIcon({
                iconUrl: "spotify.png",
                iconRetinaUrl: "spotify.png",
                iconSize: point(50, 50),
            })}
        >
            <Popup>
                <List dense={true}>
                    <ListItem>
                        <ListItemIcon>
                            <Avatar alt={title} src={"spotify.png"}/>
                        </ListItemIcon>
                        <ListItemText primary={title}/>
                    </ListItem>
                    {
                        LIST_PROPERTIES
                            .map(({key, label, Icon}) =>
                                <ListItem key={key}>
                                    <ListItemIcon>
                                        <Icon style={{color: "black"}}/>
                                    </ListItemIcon>
                                    <ListItemText
                                        primary={<span>
                                        {properties[key]}<br/>
                                        <label style={{fontSize: "xx-small"}}>({label})</label>
                                    </span>}
                                    />
                                </ListItem>
                            )
                    }

                </List>

            </Popup>
        </Marker>
    )
}
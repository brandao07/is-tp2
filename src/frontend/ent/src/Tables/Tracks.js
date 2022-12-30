import {useEffect, useState} from "react";
import {
    CircularProgress,
    Pagination,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow
} from "@mui/material";
import axios from "axios";

let tracks = []


function Tracks() {
    axios.get(`${process.env.REACT_APP_API_ENTITIES_URL}/api/tracks/`).then((response) => {
        console.log(response.data)
        tracks = response.data["Tracks"]
    }).catch((error) => {
        console.log(error)
    })
    const PAGE_SIZE = 10;
    const [page, setPage] = useState(1);
    const [data, setData] = useState(null);
    const [maxDataSize, setMaxDataSize] = useState(tracks.length);

    useEffect(() => {
        setData(null);
        setTimeout(() => {
            console.log(`fetching from ${process.env.REACT_APP_API_ENTITIES_URL}`)
            setData(tracks.filter((item, index) => Math.floor(index / PAGE_SIZE) === (page - 1)));
        }, 500);
    }, [page])

    return (
        <>
            <h1>Tracks</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" width={"1px"} align="center">ID</TableCell>
                            <TableCell>Title</TableCell>
                            <TableCell align="center">Date</TableCell>
                            <TableCell align="center">Region</TableCell>
                            <TableCell align="center">Rank</TableCell>
                            <TableCell align="center">Streams</TableCell>
                            <TableCell align="center">Artist</TableCell>
                            <TableCell align="center">Trend</TableCell>
                            <TableCell align="center">URL</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            data ?
                                data.map((row) => (
                                    <TableRow
                                        key={row.id}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.id}</TableCell>
                                        <TableCell component="td" scope="row">
                                            {row.title}
                                        </TableCell>
                                        <TableCell component="td" align="center" scope="row">
                                            {row.date}
                                        </TableCell>
                                         <TableCell component="td" align="center" scope="row">
                                            {row.region}
                                        </TableCell>
                                         <TableCell component="td" align="center" scope="row">
                                            {row.rank}
                                        </TableCell>
                                         <TableCell component="td" align="center" scope="row">
                                            {row.streams}
                                        </TableCell>
                                         <TableCell component="td" align="center" scope="row">
                                            {row.artist}
                                        </TableCell>
                                         <TableCell component="td" align="center" scope="row">
                                            {row.trend}
                                        </TableCell>
                                         <TableCell component="td" align="center" scope="row">
                                            {row.url}
                                        </TableCell>
                                    </TableRow>
                                ))
                                :
                                <TableRow>
                                    <TableCell colSpan={3}>
                                        <CircularProgress/>
                                    </TableCell>
                                </TableRow>
                        }
                    </TableBody>
                </Table>
            </TableContainer>
            {
                maxDataSize && <div style={{background: "black", padding: "1rem"}}>
                    <Pagination style={{color: "black"}}
                                variant="outlined" shape="rounded"
                                color={"primary"}
                                onChange={(e, v) => {
                                    setPage(v)
                                }}
                                page={page}
                                count={Math.ceil(maxDataSize / PAGE_SIZE)}
                    />
                </div>
            }


        </>
    );
}

export default Tracks;

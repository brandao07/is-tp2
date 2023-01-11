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

let info = []

function TracksCount() {
    axios.get(`${process.env.REACT_APP_API_PROC_URL}/api/tracks/artists`).then((response) => {
        console.log(response.data)
        info = response.data["Info"]
    }).catch((error) => {
        console.log(error)
    })
    const PAGE_SIZE = 10;
    const [page, setPage] = useState(1);
    const [data, setData] = useState(null);
    const [maxDataSize, setMaxDataSize] = useState(info.length);

    useEffect(() => {
        setData(null);
        setTimeout(() => {
            console.log(`fetching from ${URL}`)
            setData(info.filter((item, index) => Math.floor(index / PAGE_SIZE) === (page - 1)));
        }, 500);
    }, [page])

    return (
        <>
            <h1>Tracks Count By Artists</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" align="center">Artist</TableCell>
                            <TableCell>Tracks</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            data ?
                                data.map((row) => (
                                    <TableRow
                                        key={row.artist_name}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.artist_name}</TableCell>
                                        <TableCell component="td" scope="row">
                                            {row.tracks}
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

export default TracksCount;

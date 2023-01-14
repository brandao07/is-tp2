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
import {useQuery} from "@apollo/client";
import {LOAD_ARTIST_STREAMS} from "../GraphQL/Queries";

let infoREST = []
let infoGraphQL = []

function ArtistsStreams() {
    const {data} = useQuery(LOAD_ARTIST_STREAMS);
    const PAGE_SIZE = 10;
    const [page, setPage] = useState(1);
    const [dataREST, setDataREST] = useState(null);
    const [dataGraphQL, setDataGraphQL] = useState(null);
    const [maxDataSize, setMaxDataSize] = useState(infoREST.length);
    console.log(`fetching from ${process.env.REACT_APP_API_PROC_URL}`)
    axios.get(`${process.env.REACT_APP_API_PROC_URL}/api/streams`).then((response) => {
        infoREST = response.data["Info"]
    }).catch((error) => {
        console.log(error)
    })
    if (data) {
        console.log(`fetching from ${process.env.REACT_APP_API_GRAPHQL_URL}`)
        infoGraphQL = data.artistStreams
    }
    useEffect(() => {
        setTimeout(() => {
            setDataREST(infoREST.filter((item, index) => Math.floor(index / PAGE_SIZE) === (page - 1)));
            setDataGraphQL(infoGraphQL.filter((item, index) => Math.floor(index / PAGE_SIZE) === (page - 1)));
        }, 500);
    }, [page])

    return (
        <>
            <h1>Streams REST</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" align="center">Artist</TableCell>
                            <TableCell>Streams</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            dataREST ?
                                dataREST.map((row) => (
                                    <TableRow
                                        key={row.artist_name}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.artist_name}</TableCell>
                                        <TableCell component="td" scope="row">
                                            {row.streams}
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

            <h1>Streams GraphQL</h1>

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
                            dataGraphQL ?
                                dataGraphQL.map((row) => (
                                    <TableRow
                                        key={row.artistName}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.artistName}</TableCell>
                                        <TableCell component="td" scope="row">
                                            {row.streams}
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

export default ArtistsStreams;

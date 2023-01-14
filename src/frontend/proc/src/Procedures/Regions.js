import React, {useState} from "react";
import {
    Button,
    CircularProgress,
    Container,
    Pagination,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    TextField
} from "@mui/material";
import axios from "axios";
import {useLazyQuery} from "@apollo/client";
import {LOAD_BY_REGION} from "../GraphQL/Queries";

let info = []

function Regions() {
    const [searchRegion, setSearchRegion] = useState("");
    const PAGE_SIZE = 10;
    const [page, setPage] = useState(1);
    const [dataREST, setDataREST] = useState(null);
    const [dataGraphQL, setDataGraphQL] = useState(null);
    const [maxDataSize, setMaxDataSize] = useState(info.length);

    const [getTracks] = useLazyQuery(LOAD_BY_REGION);
    const handleClick = () => {
        getTracks({variables: {name: searchRegion}}).then((response) => {
            setDataGraphQL(response.data.regionTracks.filter((item, index) => Math.floor(index / PAGE_SIZE) === (page - 1)));
        })
        axios.get(`${process.env.REACT_APP_API_PROC_URL}/api/regions?region_name=${searchRegion}`).then((response) => {
            setDataREST(response.data["Info"].filter((item, index) => Math.floor(index / PAGE_SIZE) === (page - 1)))
        }).catch((error) => {
            console.log(error)
        })
    }

    return (
        <>
            <h1>Regions</h1>

            <Container maxWidth="100%"
                       sx={{
                           backgroundColor: 'background.default',
                           padding: "2rem",
                           borderRadius: "1rem",
                           marginBottom: "2rem"
                       }}>

                <h2 style={{color: "white"}}>Search</h2>
                <form autoComplete="off" noValidate>
                    <TextField
                        style={{margin: 10}}
                        color="primary"
                        id="message"
                        name="message"
                        variant="outlined"
                        label="Region"
                        onChange={(e) => setSearchRegion(e.target.value)}
                        fullWidth
                    />
                    <Button type="button" onClick={handleClick} variant="contained"
                            style={{margin: 10, color: "white"}}
                            sx={{width: 200, padding: 1, margin: 2, size: "large", backgroundColor: "gray"}}
                    >Search</Button>
                </form>

            </Container>

            <h1>Tracks REST</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" align="center">ID</TableCell>
                            <TableCell align="center">Artist</TableCell>
                            <TableCell align="center">Date</TableCell>
                            <TableCell align="center">Rank</TableCell>
                            <TableCell align="center">Region</TableCell>
                            <TableCell align="center">Streams</TableCell>
                            <TableCell align="center">Title</TableCell>
                            <TableCell align="center">Trend</TableCell>
                            <TableCell align="center">Url</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            dataREST ?
                                dataREST.map((row) => (
                                    <TableRow
                                        key={row.id}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.id}</TableCell>
                                        <TableCell align="center">{row.artist_name}</TableCell>
                                        <TableCell align="center">{row.date}</TableCell>
                                        <TableCell align="center">{row.rank}</TableCell>
                                        <TableCell align="center">{row.region_name}</TableCell>
                                        <TableCell align="center">{row.streams}</TableCell>
                                        <TableCell align="center">{row.title}</TableCell>
                                        <TableCell align="center">{row.trend}</TableCell>
                                        <TableCell align="center">{row.url}</TableCell>
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

            <h1>Tracks GraphQL</h1>

            <TableContainer component={Paper}>
                <Table sx={{minWidth: 650}} aria-label="simple table">
                    <TableHead>
                        <TableRow>
                            <TableCell component="th" align="center">ID</TableCell>
                            <TableCell align="center">Artist</TableCell>
                            <TableCell align="center">Date</TableCell>
                            <TableCell align="center">Rank</TableCell>
                            <TableCell align="center">Region</TableCell>
                            <TableCell align="center">Streams</TableCell>
                            <TableCell align="center">Title</TableCell>
                            <TableCell align="center">Trend</TableCell>
                            <TableCell align="center">Url</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {
                            dataGraphQL ?
                                dataGraphQL.map((row) => (
                                    <TableRow
                                        key={row.id}
                                        style={{background: "gray", color: "black"}}
                                    >
                                        <TableCell component="td" align="center">{row.id}</TableCell>
                                        <TableCell align="center">{row.artistName}</TableCell>
                                        <TableCell align="center">{row.date}</TableCell>
                                        <TableCell align="center">{row.rank}</TableCell>
                                        <TableCell align="center">{row.regionName}</TableCell>
                                        <TableCell align="center">{row.streams}</TableCell>
                                        <TableCell align="center">{row.title}</TableCell>
                                        <TableCell align="center">{row.trend}</TableCell>
                                        <TableCell align="center">{row.url}</TableCell>
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

export default Regions;


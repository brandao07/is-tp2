import {gql} from "@apollo/client"

export const LOAD_ARTIST_STREAMS = gql`
    query{
        artistStreams {
            artistName
            streams
        }
    }
`;

export const LOAD_ARTIST_AMOUNT = gql`
    query{
        artistAmount {
            artistName
            amount
        }
    }
`

export const LOAD_BY_REGION_ARTIST = gql`
    query Tracks1 ($regionName: String!, $artistName: String!){
        regionArtistTracks(regionName:$regionName, artistName:$artistName) {
            id
            title
            url
            streams
            rank
            date
            trend
            artistName
            regionName
        }
    }
`

export const LOAD_BY_REGION = gql`
    query Tracks2 ($name: String!) {
        regionTracks (name: $name) {
            id
            title
            url
            streams
            rank
            date
            trend
            artistName
            regionName
        }
    }
`
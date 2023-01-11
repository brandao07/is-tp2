import Regions from "../Procedures/Regions";
import TracksCount from "../Procedures/TracksCount";
import ArtistsStreams from "../Procedures/ArtistsStreams";
import ArtistRegion from "../Procedures/ArtistRegion";



const Sections = [

    {
        id: "find_by_regions",
        label: "Find by Regions",
        content: <Regions/>
    },

    {
        id: "tracks_count",
        label: "Tracks Count",
        content: <TracksCount/>
    },

    {
        id: "artists_streams",
        label: "Artists Streams",
        content: <ArtistsStreams/>
    },

    {
        id: "artists_region",
        label: "Track by Artists and Region",
        content: <ArtistRegion/>
    }

];

export default Sections;
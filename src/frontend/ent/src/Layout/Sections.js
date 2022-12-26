import Regions from "../Tables/Regions";
import Artists from "../Tables/Artists";
import Tracks from "../Tables/Tracks";

const Sections = [

    {
        id: "tracks",
        label: "Tracks",
        content: <Tracks/>
    },

    {
        id: "regions",
        label: "Regions",
        content: <Regions/>
    },

    {
        id: "artists",
        label: "Artists",
        content: <Artists/>
    }

];

export default Sections;
CREATE
EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE
EXTENSION IF NOT EXISTS POSTGIS;
CREATE
EXTENSION IF NOT EXISTS POSTGIS_TOPOLOGY;

create table if not exists public.regions
(
    id uuid default uuid_generate_v4
(
) not null
    constraint regions_pk
    primary key,
    created_on date default now
(
) not null,
    updated_on date default now
(
) not null,
    is_deleted boolean default false not null,
    name varchar not null,
    lat double precision,
    lon double precision,
    geom geometry
    );

alter table public.regions
    owner to is;

create table if not exists public.charts
(
    id uuid default uuid_generate_v4
(
) not null
    constraint charts_pk
    primary key,
    created_on time default now
(
) not null,
    updated_on date default now
(
) not null,
    is_deleted boolean default false not null,
    name varchar not null
    );

alter table public.charts
    owner to is;

create table if not exists public.artists
(
    id uuid default uuid_generate_v4
(
) not null
    constraint artists_pk
    primary key,
    created_on date default now
(
) not null,
    updated_on date default now
(
) not null,
    is_deleted boolean default false not null,
    name varchar
    );

alter table public.artists
    owner to is;

create table if not exists public.trends
(
    id uuid default uuid_generate_v4
(
) not null
    constraint trends_pk
    primary key,
    created_on date default now
(
) not null,
    updated_on date default now
(
) not null,
    is_deleted boolean default false not null,
    name varchar not null
    );

alter table public.trends
    owner to is;

create table if not exists public.tracks
(
    id uuid default uuid_generate_v4
(
) not null
    constraint tracks_pk
    primary key,
    created_on date default now
(
) not null,
    updated_on date default now
(
) not null,
    is_deleted boolean default false not null,
    title varchar not null,
    url varchar not null,
    streams varchar not null,
    rank varchar not null,
    id_artist uuid not null
    constraint tracks_artists_id_fk
    references public.artists,
    id_trend uuid not null
    constraint tracks_trends_id_fk
    references public.trends
    );

alter table public.tracks
    owner to is;

create table if not exists public.dates
(
    id uuid default uuid_generate_v4
(
) not null
    constraint dates_pk
    primary key,
    created_on date default now
(
) not null,
    updated_on date default now
(
) not null,
    is_deleted boolean default false not null,
    registered_date date not null,
    id_chart uuid not null
    constraint dates___fk
    references public.charts
    );

alter table public.dates
    owner to is;

create table if not exists public.regions_dates
(
    id uuid default uuid_generate_v4
(
) not null
    constraint regions_dates_pk
    primary key,
    id_region uuid not null
    constraint regions_dates_regions_id_fk
    references public.regions,
    id_date uuid not null
    constraint regions_dates_dates_id_fk
    references public.dates
    );

alter table public.regions_dates
    owner to is;

create table if not exists public.regions_dates_tracks
(
    id_region_date
    uuid
    not
    null
    constraint
    regions_dates_tracks_regions_dates_id_fk
    references
    public
    .
    regions_dates,
    id_track
    uuid
    not
    null
    constraint
    regions_dates_tracks_tracks_id_fk
    references
    public
    .
    tracks,
    constraint
    regions_dates_tracks_pk
    primary
    key
(
    id_region_date,
    id_track
)
    );

alter table public.regions_dates_tracks
    owner to is;

CREATE
EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE
EXTENSION IF NOT EXISTS POSTGIS;
CREATE
EXTENSION IF NOT EXISTS POSTGIS_TOPOLOGY;

create table if not exists public.regions
(
    id         uuid    default uuid_generate_v4() not null
        constraint regions_pk
            primary key,
    name       varchar                            not null
        constraint regions_pk2
            unique,
    geom       geometry                           not null
        constraint regions_pk3
            unique,
    created_at date    default now()              not null,
    is_deleted boolean default false              not null
);

alter table public.regions
    owner to is;

create table if not exists public.artists
(
    id         uuid    default uuid_generate_v4() not null
        constraint artists_pk
            primary key,
    name       varchar                            not null,
    created_at date    default now()              not null,
    is_deleted boolean default false              not null
);

alter table public.artists
    owner to is;

create table if not exists public.tracks
(
    id         uuid    default uuid_generate_v4() not null
        constraint tracks_pk
            primary key,
    title      varchar                            not null,
    url        varchar                            not null,
    streams    varchar                            not null,
    date       date                               not null,
    trend      varchar                            not null,
    rank       integer                            not null,
    artists_id uuid                               not null
        constraint tracks_artists_id_fk
            references public.artists,
    regions_id uuid                               not null
        constraint tracks_regions_id_fk
            references public.regions,
    created_at date    default now()              not null,
    is_deleted boolean default false              not null
);

alter table public.tracks
    owner to is;


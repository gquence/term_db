--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5 (Ubuntu 11.5-3.pgdg19.04+1)
-- Dumped by pg_dump version 11.5 (Ubuntu 11.5-3.pgdg19.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: bookings; Type: SCHEMA; Schema: -; Owner: test_user
--

CREATE SCHEMA bookings;


ALTER SCHEMA bookings OWNER TO test_user;

--
-- Name: device_types; Type: TYPE; Schema: public; Owner: test_user
--

CREATE TYPE public.device_types AS ENUM (
    'laptop',
    'pc',
    'printer',
    'phone',
    'instrument',
    'other'
);


ALTER TYPE public.device_types OWNER TO test_user;

--
-- Name: e_employed_status; Type: TYPE; Schema: public; Owner: test_user
--

CREATE TYPE public.e_employed_status AS ENUM (
    'employed',
    'fired',
    'intern'
);


ALTER TYPE public.e_employed_status OWNER TO test_user;

--
-- Name: e_status; Type: TYPE; Schema: public; Owner: test_user
--

CREATE TYPE public.e_status AS ENUM (
    'waiting',
    'in_progress',
    'failure',
    'success'
);


ALTER TYPE public.e_status OWNER TO test_user;

--
-- Name: palette; Type: TYPE; Schema: public; Owner: test_user
--

CREATE TYPE public.palette AS ENUM (
    'RGB',
    'CMYK',
    'WB',
    'other'
);


ALTER TYPE public.palette OWNER TO test_user;

--
-- Name: paper_format; Type: TYPE; Schema: public; Owner: test_user
--

CREATE TYPE public.paper_format AS ENUM (
    'A1',
    'A2',
    'A3',
    'A4',
    'A5',
    'custom'
);


ALTER TYPE public.paper_format OWNER TO test_user;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: devices; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.devices (
    model text NOT NULL,
    maker text NOT NULL,
    type public.device_types NOT NULL,
    purchase_date date DEFAULT CURRENT_DATE NOT NULL,
    price money DEFAULT 0 NOT NULL
);


ALTER TABLE public.devices OWNER TO test_user;

--
-- Name: employees; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.employees (
    id_employee integer NOT NULL,
    surname text NOT NULL,
    name text NOT NULL,
    "position" text,
    employed_status public.e_employed_status DEFAULT 'employed'::public.e_employed_status NOT NULL
);


ALTER TABLE public.employees OWNER TO test_user;

--
-- Name: employees_id_employee_seq; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.employees_id_employee_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.employees_id_employee_seq OWNER TO test_user;

--
-- Name: employees_id_employee_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: test_user
--

ALTER SEQUENCE public.employees_id_employee_seq OWNED BY public.employees.id_employee;


--
-- Name: id_instrument; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.id_instrument
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.id_instrument OWNER TO test_user;

--
-- Name: id_laptop; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.id_laptop
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.id_laptop OWNER TO test_user;

--
-- Name: id_pc; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.id_pc
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.id_pc OWNER TO test_user;

--
-- Name: id_phone; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.id_phone
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.id_phone OWNER TO test_user;

--
-- Name: id_printer; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.id_printer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.id_printer OWNER TO test_user;

--
-- Name: id_project; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.id_project
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.id_project OWNER TO test_user;

--
-- Name: instrument; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.instrument (
    id_instrument integer DEFAULT nextval('public.id_instrument'::regclass) NOT NULL,
    model text NOT NULL,
    usability boolean DEFAULT false NOT NULL
);


ALTER TABLE public.instrument OWNER TO test_user;

--
-- Name: laptops; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.laptops (
    id_laptop integer DEFAULT nextval('public.id_laptop'::regclass) NOT NULL,
    model text NOT NULL,
    speed real DEFAULT 1 NOT NULL,
    ram integer DEFAULT 128 NOT NULL,
    hdd integer DEFAULT 32 NOT NULL,
    id_employee_in_use integer
);


ALTER TABLE public.laptops OWNER TO test_user;

--
-- Name: printers; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.printers (
    id_printer integer DEFAULT nextval('public.id_printer'::regclass) NOT NULL,
    model text NOT NULL,
    format public.paper_format NOT NULL,
    color_palette public.palette NOT NULL
);


ALTER TABLE public.printers OWNER TO test_user;

--
-- Name: projects; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.projects (
    id_project integer DEFAULT nextval('public.id_project'::regclass) NOT NULL,
    name text NOT NULL,
    id_team integer NOT NULL,
    status public.e_status NOT NULL,
    description character varying(255) NOT NULL,
    id_instrument integer NOT NULL,
    deadline date DEFAULT (CURRENT_DATE + 1) NOT NULL,
    contract_number text NOT NULL
);


ALTER TABLE public.projects OWNER TO test_user;

--
-- Name: team_info; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.team_info (
    id_team integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.team_info OWNER TO test_user;

--
-- Name: team_info_id_team_seq; Type: SEQUENCE; Schema: public; Owner: test_user
--

CREATE SEQUENCE public.team_info_id_team_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.team_info_id_team_seq OWNER TO test_user;

--
-- Name: team_info_id_team_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: test_user
--

ALTER SEQUENCE public.team_info_id_team_seq OWNED BY public.team_info.id_team;


--
-- Name: team_members; Type: TABLE; Schema: public; Owner: test_user
--

CREATE TABLE public.team_members (
    id_employee integer,
    role text NOT NULL,
    team_id integer
);


ALTER TABLE public.team_members OWNER TO test_user;

--
-- Name: employees id_employee; Type: DEFAULT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.employees ALTER COLUMN id_employee SET DEFAULT nextval('public.employees_id_employee_seq'::regclass);


--
-- Name: team_info id_team; Type: DEFAULT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.team_info ALTER COLUMN id_team SET DEFAULT nextval('public.team_info_id_team_seq'::regclass);


--
-- Data for Name: devices; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.devices (model, maker, type, purchase_date, price) FROM stdin;
gw4g2BrEVmdJUAS5	Black and Decker	instrument	2019-12-22	90,45 ₽
4mT3p	BOSCH	instrument	2019-12-22	79,56 ₽
SiMxPru	Elitech	instrument	2019-12-22	124,47 ₽
VNUgp8Y	Hitachi	instrument	2019-12-22	100,33 ₽
PvuBD	Ryobi	instrument	2019-12-22	124,00 ₽
aINrjfQpu1upJ5gr	Black and Decker	instrument	2019-12-22	90,30 ₽
6cJYK	BOSCH	instrument	2019-12-22	120,68 ₽
AAgOAfr	Elitech	instrument	2019-12-22	124,98 ₽
3uSaktQ	Hitachi	instrument	2019-12-22	79,38 ₽
owR7N	Ryobi	instrument	2019-12-22	100,27 ₽
OmDoApGVdTI9ixYT	Black and Decker	instrument	2019-12-22	79,87 ₽
tGCgQ	BOSCH	instrument	2019-12-22	79,46 ₽
6q6bezE	Elitech	instrument	2019-12-22	100,21 ₽
iRa3tEl	Hitachi	instrument	2019-12-22	100,15 ₽
bQOFt	Ryobi	instrument	2019-12-22	124,71 ₽
JcGk	ACER	laptop	2019-12-23	565,74 ₽
SfoHMJlAwl	ALIEN_WARE	laptop	2019-12-23	1 000,96 ₽
bTWh	ASUS	laptop	2019-12-23	900,81 ₽
2O85	DELL	laptop	2019-12-23	1 750,69 ₽
eOb8B	DIGMA	laptop	2019-12-23	565,69 ₽
wInfVhw	FUJITSU	laptop	2019-12-23	1 750,80 ₽
2N	HP	laptop	2019-12-23	1 000,26 ₽
lx6m3y	HUAWEI	laptop	2019-12-23	900,99 ₽
fTg9W4	LENOVO	laptop	2019-12-23	1 750,66 ₽
Ul6	MSI	laptop	2019-12-23	1 750,97 ₽
LgruX8KIi	PRESTIGIO	laptop	2019-12-23	350,39 ₽
6dRi	ACER	laptop	2019-12-23	900,76 ₽
28AKzNJHnu	ALIEN_WARE	laptop	2019-12-23	565,32 ₽
9Q2J	ASUS	laptop	2019-12-23	565,64 ₽
ysXh	DELL	laptop	2019-12-23	350,46 ₽
cQPS	ACER	laptop	2019-12-23	1 750,47 ₽
AJqWZXdlvo	ALIEN_WARE	laptop	2019-12-23	565,20 ₽
KleE	ASUS	laptop	2019-12-23	350,45 ₽
i5WK	DELL	laptop	2019-12-23	350,96 ₽
Fqfsp	DIGMA	laptop	2019-12-23	350,97 ₽
QX3SPrr	FUJITSU	laptop	2019-12-23	350,50 ₽
9d	HP	laptop	2019-12-23	799,39 ₽
HXgQWR	HUAWEI	laptop	2019-12-23	900,81 ₽
mgvt6j	LENOVO	laptop	2019-12-23	1 750,86 ₽
dn4	MSI	laptop	2019-12-23	350,49 ₽
wjOpRWED0	PRESTIGIO	laptop	2019-12-23	900,17 ₽
MGTK	ACER	laptop	2019-12-23	799,60 ₽
pJ8WYfXp8U	ALIEN_WARE	laptop	2019-12-23	799,10 ₽
lhpz	ASUS	laptop	2019-12-23	799,14 ₽
HOX8	DELL	laptop	2019-12-23	799,68 ₽
PYCu9	DIGMA	laptop	2019-12-23	350,86 ₽
o4g9Wkp	FUJITSU	laptop	2019-12-23	900,20 ₽
b7	HP	laptop	2019-12-23	350,56 ₽
f1L8Ja	HUAWEI	laptop	2019-12-23	1 750,49 ₽
b0yw6E	LENOVO	laptop	2019-12-23	565,68 ₽
sf3	MSI	laptop	2019-12-23	350,95 ₽
AGuF1i6I5	PRESTIGIO	laptop	2019-12-23	565,52 ₽
jpwf	ACER	laptop	2019-12-23	799,39 ₽
Z1ym2Ov6d7	ALIEN_WARE	laptop	2019-12-23	799,58 ₽
6UML	ASUS	laptop	2019-12-23	1 750,46 ₽
qzxU	DELL	laptop	2019-12-23	1 000,76 ₽
HV7Ty	DIGMA	laptop	2019-12-23	565,20 ₽
1DAB4hJ	FUJITSU	laptop	2019-12-23	350,13 ₽
DI	HP	laptop	2019-12-23	799,19 ₽
deLYiN	HUAWEI	laptop	2019-12-23	900,69 ₽
8LAyOX	LENOVO	laptop	2019-12-23	565,11 ₽
dsg	MSI	laptop	2019-12-23	799,20 ₽
JGBhPDmzA	PRESTIGIO	laptop	2019-12-23	350,58 ₽
25Vi	ACER	laptop	2019-12-23	900,78 ₽
CfUwkojB6X	ALIEN_WARE	laptop	2019-12-23	799,20 ₽
mhV1	ASUS	laptop	2019-12-23	1 750,67 ₽
lu8B	DELL	laptop	2019-12-23	799,68 ₽
vNLns	DIGMA	laptop	2019-12-23	900,10 ₽
H89pnkb	FUJITSU	laptop	2019-12-23	1 000,15 ₽
ZN	HP	laptop	2019-12-23	900,80 ₽
dANJY0	HUAWEI	laptop	2019-12-23	565,36 ₽
i6e5Vt	LENOVO	laptop	2019-12-23	1 000,17 ₽
Dm3	MSI	laptop	2019-12-23	799,80 ₽
giQ1UVzY9	PRESTIGIO	laptop	2019-12-23	799,39 ₽
no5F	ACER	laptop	2019-12-23	565,51 ₽
qszaad96kv	ALIEN_WARE	laptop	2019-12-23	799,34 ₽
uQbk	ASUS	laptop	2019-12-23	900,22 ₽
9Jyk	DELL	laptop	2019-12-23	1 750,42 ₽
p5Jku	DIGMA	laptop	2019-12-23	900,72 ₽
Hlu0pWa	FUJITSU	laptop	2019-12-23	900,42 ₽
Uc14	ACER	laptop	2019-12-23	799,10 ₽
dak5x6Eck5	ALIEN_WARE	laptop	2019-12-23	799,25 ₽
fxxy	ASUS	laptop	2019-12-23	900,51 ₽
5UGc	DELL	laptop	2019-12-23	900,86 ₽
Cd7MQ	DIGMA	laptop	2019-12-23	350,88 ₽
weukKdA	FUJITSU	laptop	2019-12-23	1 000,38 ₽
HQ	HP	laptop	2019-12-23	350,96 ₽
3ZlVX0	HUAWEI	laptop	2019-12-23	1 000,38 ₽
4Z5zbc	LENOVO	laptop	2019-12-23	799,36 ₽
9nr	MSI	laptop	2019-12-23	1 000,38 ₽
cRUITBZmG	PRESTIGIO	laptop	2019-12-23	1 750,11 ₽
EfnQ	ACER	laptop	2019-12-23	799,63 ₽
WQKUyHjJeh	ALIEN_WARE	laptop	2019-12-23	350,53 ₽
XAsJ	ASUS	laptop	2019-12-23	350,31 ₽
si2q	DELL	laptop	2019-12-23	565,20 ₽
M2MZ0	DIGMA	laptop	2019-12-23	799,70 ₽
bZYIYvq	FUJITSU	laptop	2019-12-23	1 750,31 ₽
eu	HP	laptop	2019-12-23	1 000,57 ₽
0v7add	HUAWEI	laptop	2019-12-23	900,34 ₽
A3pOnC	LENOVO	laptop	2019-12-23	350,95 ₽
H35	MSI	laptop	2019-12-23	565,46 ₽
EwgJTawjb	PRESTIGIO	laptop	2019-12-23	565,10 ₽
ydGW	ACER	laptop	2019-12-23	1 000,67 ₽
ZglnXPpwJN	ALIEN_WARE	laptop	2019-12-23	1 000,61 ₽
SzHl	ASUS	laptop	2019-12-23	1 000,71 ₽
Z6o7	DELL	laptop	2019-12-23	565,95 ₽
EAbG0	DIGMA	laptop	2019-12-23	350,52 ₽
jpGKws0	FUJITSU	laptop	2019-12-23	350,83 ₽
OT	HP	laptop	2019-12-23	799,34 ₽
V6UH0h	HUAWEI	laptop	2019-12-23	900,12 ₽
lX7j4c	LENOVO	laptop	2019-12-23	565,11 ₽
yRe	MSI	laptop	2019-12-23	900,65 ₽
hrJoAYcs8	PRESTIGIO	laptop	2019-12-23	350,93 ₽
jS8y	ACER	laptop	2019-12-23	565,99 ₽
X9NP8i8H8Z	ALIEN_WARE	laptop	2019-12-23	565,75 ₽
5vFD	ASUS	laptop	2019-12-23	900,00 ₽
Fgty	DELL	laptop	2019-12-23	1 000,57 ₽
sF96u	DIGMA	laptop	2019-12-23	1 750,81 ₽
NJAPQyE	FUJITSU	laptop	2019-12-23	565,29 ₽
RZ	HP	laptop	2019-12-23	350,42 ₽
TgRZNQ	HUAWEI	laptop	2019-12-23	350,71 ₽
eY2D0f	LENOVO	laptop	2019-12-23	350,42 ₽
M1t	MSI	laptop	2019-12-23	1 000,37 ₽
9HospcOoe	PRESTIGIO	laptop	2019-12-23	1 000,35 ₽
EVua	ACER	laptop	2019-12-23	1 000,46 ₽
WTMdcgrRm6	ALIEN_WARE	laptop	2019-12-23	1 000,83 ₽
PLUm	ASUS	laptop	2019-12-23	799,72 ₽
1Izy	DELL	laptop	2019-12-23	799,33 ₽
ctYoW	DIGMA	laptop	2019-12-23	1 000,98 ₽
OTbgrtA	FUJITSU	laptop	2019-12-23	350,74 ₽
Gw	HP	laptop	2019-12-23	799,41 ₽
MAdCE6	HUAWEI	laptop	2019-12-23	900,75 ₽
NFyFhq	LENOVO	laptop	2019-12-23	350,43 ₽
SKQ	MSI	laptop	2019-12-23	350,62 ₽
CU9lJ2Kwb	PRESTIGIO	laptop	2019-12-23	1 000,98 ₽
FlNi	ACER	laptop	2019-12-23	799,86 ₽
9RUT8b1qgd	ALIEN_WARE	laptop	2019-12-23	799,68 ₽
bcwb	ASUS	laptop	2019-12-23	350,13 ₽
YBwN	DELL	laptop	2019-12-23	1 750,60 ₽
8FGHj	DIGMA	laptop	2019-12-23	900,91 ₽
HnN6vF3I	Canon	printer	2019-12-23	350,46 ₽
eNjCylvm	Epson	printer	2019-12-23	165,18 ₽
X2wuG	HP	printer	2019-12-23	165,53 ₽
T1lstRc005	Kyocera	printer	2019-12-23	500,81 ₽
ecClQCFs	Canon	printer	2019-12-23	200,75 ₽
JKMpbML9	Epson	printer	2019-12-23	200,71 ₽
WW4vA	HP	printer	2019-12-23	400,71 ₽
zRm0w5PNjg	Kyocera	printer	2019-12-23	500,61 ₽
5SqBllEH	Canon	printer	2019-12-23	350,75 ₽
O5uwTudM	Epson	printer	2019-12-23	200,49 ₽
crhD1	HP	printer	2019-12-23	165,79 ₽
33Dq7q7RVP	Kyocera	printer	2019-12-23	200,75 ₽
WWjvpsIv	Canon	printer	2019-12-23	100,82 ₽
UoyMPmZ2	Epson	printer	2019-12-23	100,96 ₽
C0zsl	HP	printer	2019-12-23	100,59 ₽
\.


--
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.employees (id_employee, surname, name, "position", employed_status) FROM stdin;
6	Emiko	Earwood	CEO	employed
7	Aiko	Aubin	CTO	employed
8	Elliott	Eshbaugh	Accountant	employed
9	Jae	Jeffreys	System Administrator	employed
10	Jerrie	Jardin	Chief Engineer	employed
11	Taylor	Taketa	Chief Engineer	employed
12	Laurene	Lebow	Chief Engineer	employed
13	Machelle	Marquis	Chief Engineer	employed
14	Mika	Monroe	Chief Engineer	employed
15	Marylynn	Merkle	Engineer	employed
16	Karleen	Kimmell	Engineer	employed
17	Chet	Calabrese	Engineer	employed
18	Eleonore	Emerson	Engineer	employed
19	Mariette	Meader	Engineer	employed
20	Bennett	Black	Engineer	employed
21	Tasha	Tardugno	Engineer	employed
22	Shana	Sharpton	Engineer	employed
23	David	Doty	Engineer	employed
24	Ariane	Andresen	Engineer	employed
25	Demetria	Drum	Engineer	employed
26	Olimpia	Orman	Engineer	employed
27	Mervin	Minelli	Engineer	employed
28	Kam	Kittleson	Engineer	employed
29	Yang	Yankey	Engineer	employed
30	Willie	Weld	Gen. Worker	employed
31	Ayana	Argueta	Gen. Worker	employed
32	Tawana	Tallent	Gen. Worker	employed
33	Lanelle	Lasker	Gen. Worker	employed
34	Nicol	Nickles	Gen. Worker	employed
35	Loyce	Lenzi	Gen. Worker	employed
36	Tess	Trosper	Gen. Worker	employed
37	Mariella	Mallet	Gen. Worker	employed
38	Dorris	Dunkle	Gen. Worker	employed
39	Jessie	Jeremiah	Gen. Worker	employed
40	Charissa	Combest	Gen. Worker	employed
41	Vinita	Verhoeven	Gen. Worker	employed
42	Pamelia	Perri	Gen. Worker	employed
43	Nerissa	Narvaez	Gen. Worker	employed
44	Pearle	Platero	Gen. Worker	employed
45	Frederic	Fennessey	Gen. Worker	employed
46	Suzie	Sprowl	Gen. Worker	employed
47	Raleigh	Rasheed	Gen. Worker	employed
48	Vinnie	Vina	Gen. Worker	employed
49	Lou	Liddell	Gen. Worker	employed
50	Craig	Caicedo	Gen. Worker	employed
51	Stevie	Shirk	Gen. Worker	employed
52	Zenia	Zirkle	Gen. Worker	employed
53	Jacalyn	Jerrell	Gen. Worker	employed
54	Alise	Ackerman	Gen. Worker	employed
55	Carmon	Connery	Gen. Worker	employed
56	Laquita	Lutz	Gen. Worker	employed
57	Debby	Dunfee	Gen. Worker	employed
58	Elfrieda	Elfrink	Gen. Worker	employed
59	Archie	Adkison	Gen. Worker	employed
\.


--
-- Data for Name: instrument; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.instrument (id_instrument, model, usability) FROM stdin;
1	gw4g2BrEVmdJUAS5	t
2	4mT3p	t
3	SiMxPru	t
4	VNUgp8Y	t
5	PvuBD	t
6	aINrjfQpu1upJ5gr	t
7	6cJYK	t
8	AAgOAfr	t
9	3uSaktQ	t
10	owR7N	t
11	OmDoApGVdTI9ixYT	t
12	tGCgQ	t
13	6q6bezE	t
14	iRa3tEl	t
15	bQOFt	t
\.


--
-- Data for Name: laptops; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.laptops (id_laptop, model, speed, ram, hdd, id_employee_in_use) FROM stdin;
1	JcGk	2.92000008	4096	2048	\N
2	SfoHMJlAwl	3.55999994	4096	4096	\N
3	bTWh	2	32768	1024	\N
4	2O85	3.76999998	16384	256	\N
5	eOb8B	4.82000017	32768	1024	\N
6	wInfVhw	4.11000013	32768	256	\N
7	2N	2.97000003	8192	256	\N
8	lx6m3y	2.66000009	32768	2048	\N
9	fTg9W4	4.17999983	4096	2048	\N
10	Ul6	1.97000003	4096	512	\N
11	LgruX8KIi	2.67000008	4096	2048	\N
12	6dRi	4.78999996	4096	4096	\N
13	28AKzNJHnu	3.79999995	16384	512	\N
14	9Q2J	3.5	32768	4096	\N
15	ysXh	1.42999995	16384	512	\N
16	cQPS	2.93000007	16384	1024	\N
17	AJqWZXdlvo	4.75	32768	512	\N
18	KleE	2.68000007	32768	4096	\N
19	i5WK	1.66999996	4096	256	\N
20	Fqfsp	3.72000003	8192	2048	\N
21	QX3SPrr	4.69000006	4096	256	\N
22	9d	1.58000004	32768	2048	\N
23	HXgQWR	4.90999985	4096	2048	\N
24	mgvt6j	4.51000023	8192	4096	\N
25	dn4	4.78000021	8192	256	\N
26	wjOpRWED0	4.23999977	4096	4096	\N
27	MGTK	2.66000009	4096	512	\N
28	pJ8WYfXp8U	1.26999998	4096	4096	\N
29	lhpz	1.49000001	4096	2048	\N
30	HOX8	2.13000011	8192	1024	\N
31	PYCu9	2.86999989	8192	1024	\N
32	o4g9Wkp	4.73999977	32768	4096	\N
33	b7	4.73999977	32768	1024	\N
34	f1L8Ja	4.71999979	32768	512	\N
35	b0yw6E	3.17000008	8192	1024	\N
36	sf3	1.45000005	32768	2048	\N
37	AGuF1i6I5	2.6099999	4096	2048	\N
38	jpwf	3.83999991	32768	512	\N
39	Z1ym2Ov6d7	3.27999997	32768	1024	\N
40	6UML	4.51000023	4096	1024	\N
41	qzxU	4.5	32768	512	\N
42	HV7Ty	4.17999983	32768	256	\N
43	1DAB4hJ	4.9000001	4096	256	\N
44	DI	1.60000002	4096	256	\N
45	deLYiN	1.59000003	16384	512	\N
46	8LAyOX	2.11999989	16384	2048	\N
47	dsg	4.9000001	4096	2048	\N
48	JGBhPDmzA	2.45000005	4096	4096	\N
49	25Vi	2.94000006	4096	512	\N
50	CfUwkojB6X	3.1400001	32768	4096	\N
51	mhV1	1.17999995	32768	2048	\N
52	lu8B	3.13000011	16384	1024	\N
53	vNLns	1.26999998	8192	256	\N
54	H89pnkb	3.8499999	4096	2048	\N
55	ZN	4.76000023	32768	4096	\N
56	dANJY0	1.76999998	16384	512	\N
57	i6e5Vt	4.5	8192	2048	\N
58	Dm3	3.3599999	4096	256	\N
59	giQ1UVzY9	4.15999985	8192	2048	\N
60	no5F	1.61000001	8192	4096	\N
61	qszaad96kv	4.67999983	4096	4096	\N
62	uQbk	3.78999996	4096	256	\N
63	9Jyk	3.5	32768	2048	\N
64	p5Jku	3.9000001	16384	512	\N
65	Hlu0pWa	1.5	16384	1024	\N
66	Uc14	2.97000003	32768	4096	\N
67	dak5x6Eck5	1.22000003	32768	2048	\N
68	fxxy	4.61999989	4096	256	\N
69	5UGc	2.88000011	32768	512	\N
70	Cd7MQ	3.51999998	4096	2048	\N
71	weukKdA	4.69000006	16384	4096	\N
72	HQ	3.93000007	4096	2048	\N
73	3ZlVX0	2.94000006	16384	256	\N
74	4Z5zbc	1.91999996	32768	2048	\N
75	9nr	2.75999999	32768	1024	\N
76	cRUITBZmG	1.89999998	4096	1024	\N
77	EfnQ	3.9000001	8192	4096	\N
78	WQKUyHjJeh	3.3599999	4096	4096	\N
79	XAsJ	3.9000001	4096	512	\N
80	si2q	1.38	8192	256	\N
81	M2MZ0	1.34000003	8192	512	\N
82	bZYIYvq	3.75999999	8192	512	\N
83	eu	2.6099999	4096	2048	\N
84	0v7add	2.91000009	32768	1024	\N
85	A3pOnC	3.77999997	4096	256	\N
86	H35	1.22000003	16384	2048	\N
87	EwgJTawjb	2.5	8192	2048	\N
88	ydGW	4.46000004	8192	256	\N
89	ZglnXPpwJN	1.42999995	16384	1024	\N
90	SzHl	4.71999979	8192	1024	\N
91	Z6o7	1.96000004	8192	1024	\N
92	EAbG0	4.28000021	4096	256	\N
93	jpGKws0	2.38000011	32768	1024	\N
94	OT	1.29999995	32768	512	\N
95	V6UH0h	4.88000011	16384	512	\N
96	lX7j4c	1.38	8192	256	\N
97	yRe	1.65999997	8192	256	\N
98	hrJoAYcs8	3.44000006	16384	256	\N
99	jS8y	2.44000006	8192	2048	\N
100	X9NP8i8H8Z	2.98000002	16384	4096	\N
101	5vFD	1.55999994	8192	256	\N
102	Fgty	3.6099999	32768	1024	\N
103	sF96u	1.23000002	16384	2048	\N
104	NJAPQyE	3.75999999	4096	256	\N
105	RZ	1.80999994	32768	256	\N
106	TgRZNQ	4.48000002	4096	2048	\N
107	eY2D0f	3.24000001	16384	1024	\N
108	M1t	3.1400001	8192	256	\N
109	9HospcOoe	1.97000003	8192	4096	\N
110	EVua	1.74000001	8192	512	\N
111	WTMdcgrRm6	4.28999996	16384	2048	\N
112	PLUm	4.51000023	4096	4096	\N
113	1Izy	1.20000005	16384	256	\N
114	ctYoW	1.57000005	16384	1024	\N
115	OTbgrtA	4.5999999	32768	2048	\N
116	Gw	2.0999999	32768	1024	\N
117	MAdCE6	2.70000005	16384	4096	\N
118	NFyFhq	1.70000005	8192	256	\N
119	SKQ	3.70000005	8192	512	\N
120	CU9lJ2Kwb	1.22000003	16384	256	\N
121	FlNi	1.27999997	16384	2048	\N
122	9RUT8b1qgd	2.0999999	8192	512	\N
123	bcwb	1.12	32768	256	\N
124	YBwN	3.22000003	4096	256	\N
125	8FGHj	4.19000006	4096	256	\N
\.


--
-- Data for Name: printers; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.printers (id_printer, model, format, color_palette) FROM stdin;
1	HnN6vF3I	A1	CMYK
2	eNjCylvm	A2	RGB
3	X2wuG	A1	CMYK
4	T1lstRc005	A2	RGB
5	ecClQCFs	A5	WB
6	JKMpbML9	A3	RGB
7	WW4vA	A5	CMYK
8	zRm0w5PNjg	A1	RGB
9	5SqBllEH	A3	CMYK
10	O5uwTudM	A1	CMYK
11	crhD1	A2	WB
12	33Dq7q7RVP	A2	WB
13	WWjvpsIv	A1	RGB
14	UoyMPmZ2	A4	CMYK
15	C0zsl	A5	CMYK
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.projects (id_project, name, id_team, status, description, id_instrument, deadline, contract_number) FROM stdin;
2	repair or remove	1	waiting	not ez task	2	2019-10-01	2
3	rede	2	in_progress	complex task	4	2020-01-01	3
5	bad job	3	failure	bad guy	4	2018-12-12	4
1	test_proj	1	in_progress	ez task	1	2020-01-29	1
\.


--
-- Data for Name: team_info; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.team_info (id_team, name) FROM stdin;
1	nova_team
2	ssheba_meow
3	D4A_team
4	hentai_brigade
6	shishka_team
\.


--
-- Data for Name: team_members; Type: TABLE DATA; Schema: public; Owner: test_user
--

COPY public.team_members (id_employee, role, team_id) FROM stdin;
10	team_lead	1
11	team_lead	2
12	team_lead	3
13	team_lead	4
14	team_lead	6
15	middle	1
16	middle	2
17	middle	3
18	middle	4
19	middle	6
20	middle	1
21	middle	2
22	middle	3
23	middle	4
24	middle	6
25	middle	1
26	middle	2
27	middle	3
28	middle	4
29	middle	6
31	Junior	2
32	Junior	3
33	Junior	4
34	Junior	6
35	Junior	1
36	Junior	2
37	Junior	3
38	Junior	4
39	Junior	6
40	Junior	1
41	Junior	2
42	Junior	3
43	Junior	4
44	Junior	6
45	Junior	1
46	Junior	2
47	Junior	3
48	Junior	4
49	Junior	6
50	Junior	1
51	Junior	2
52	Junior	3
53	Junior	4
54	Junior	6
55	Junior	1
56	Junior	2
57	Junior	3
58	Junior	4
59	Junior	6
\.


--
-- Name: employees_id_employee_seq; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.employees_id_employee_seq', 59, true);


--
-- Name: id_instrument; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.id_instrument', 15, true);


--
-- Name: id_laptop; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.id_laptop', 125, true);


--
-- Name: id_pc; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.id_pc', 1, false);


--
-- Name: id_phone; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.id_phone', 1, false);


--
-- Name: id_printer; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.id_printer', 15, true);


--
-- Name: id_project; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.id_project', 5, true);


--
-- Name: team_info_id_team_seq; Type: SEQUENCE SET; Schema: public; Owner: test_user
--

SELECT pg_catalog.setval('public.team_info_id_team_seq', 6, true);


--
-- Name: devices devices_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.devices
    ADD CONSTRAINT devices_pkey PRIMARY KEY (model);


--
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id_employee);


--
-- Name: instrument instrument_model_key; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.instrument
    ADD CONSTRAINT instrument_model_key UNIQUE (model);


--
-- Name: instrument instrument_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.instrument
    ADD CONSTRAINT instrument_pkey PRIMARY KEY (id_instrument);


--
-- Name: laptops laptops_model_key; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.laptops
    ADD CONSTRAINT laptops_model_key UNIQUE (model);


--
-- Name: laptops laptops_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.laptops
    ADD CONSTRAINT laptops_pkey PRIMARY KEY (id_laptop);


--
-- Name: printers printers_model_key; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT printers_model_key UNIQUE (model);


--
-- Name: printers printers_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT printers_pkey PRIMARY KEY (id_printer);


--
-- Name: projects projects_contract_number_key; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_contract_number_key UNIQUE (contract_number);


--
-- Name: projects projects_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_pkey PRIMARY KEY (id_project);


--
-- Name: team_info team_info_name_key; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.team_info
    ADD CONSTRAINT team_info_name_key UNIQUE (name);


--
-- Name: team_info team_info_pkey; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.team_info
    ADD CONSTRAINT team_info_pkey PRIMARY KEY (id_team);


--
-- Name: team_members team_members_id_employee_key; Type: CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.team_members
    ADD CONSTRAINT team_members_id_employee_key UNIQUE (id_employee);


--
-- Name: instrument instrument_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.instrument
    ADD CONSTRAINT instrument_model_fkey FOREIGN KEY (model) REFERENCES public.devices(model) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: laptops laptops_id_employee_in_use_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.laptops
    ADD CONSTRAINT laptops_id_employee_in_use_fkey FOREIGN KEY (id_employee_in_use) REFERENCES public.employees(id_employee);


--
-- Name: laptops laptops_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.laptops
    ADD CONSTRAINT laptops_model_fkey FOREIGN KEY (model) REFERENCES public.devices(model) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: printers printers_model_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.printers
    ADD CONSTRAINT printers_model_fkey FOREIGN KEY (model) REFERENCES public.devices(model) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: projects projects_id_instrument_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_id_instrument_fkey FOREIGN KEY (id_instrument) REFERENCES public.instrument(id_instrument) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: projects projects_id_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_id_team_fkey FOREIGN KEY (id_team) REFERENCES public.team_info(id_team) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: team_members team_members_id_employee_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.team_members
    ADD CONSTRAINT team_members_id_employee_fkey FOREIGN KEY (id_employee) REFERENCES public.employees(id_employee) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: team_members team_members_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: test_user
--

ALTER TABLE ONLY public.team_members
    ADD CONSTRAINT team_members_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.team_info(id_team) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: TABLE devices; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.devices TO guest_user;


--
-- Name: TABLE employees; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.employees TO guest_user;


--
-- Name: TABLE instrument; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.instrument TO guest_user;


--
-- Name: TABLE laptops; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.laptops TO guest_user;


--
-- Name: TABLE printers; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.printers TO guest_user;


--
-- Name: TABLE projects; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.projects TO guest_user;


--
-- Name: TABLE team_info; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.team_info TO guest_user;


--
-- Name: TABLE team_members; Type: ACL; Schema: public; Owner: test_user
--

GRANT SELECT ON TABLE public.team_members TO guest_user;


--
-- PostgreSQL database dump complete
--


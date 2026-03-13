--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

-- Started on 2026-01-14 23:05:19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 219 (class 1259 OID 32813)
-- Name: inventories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.inventories (
    user_uuid character varying,
    item_id integer,
    inventory_id integer NOT NULL
);


ALTER TABLE public.inventories OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 41029)
-- Name: inventories_inventory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.inventories ALTER COLUMN inventory_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.inventories_inventory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 32803)
-- Name: items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.items (
    type character varying,
    name text,
    description text,
    item_id integer NOT NULL,
    icon_path character varying
);


ALTER TABLE public.items OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 32818)
-- Name: items_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.items ALTER COLUMN item_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.items_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 32808)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_uuid text NOT NULL,
    type text
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 4801 (class 0 OID 32813)
-- Dependencies: 219
-- Data for Name: inventories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.inventories OVERRIDING SYSTEM VALUE VALUES ('dc7a721e-20dc-4c6d-b9c2-086707f840d2', 1, 1);
INSERT INTO public.inventories OVERRIDING SYSTEM VALUE VALUES ('dc7a721e-20dc-4c6d-b9c2-086707f840d2', 1, 2);


--
-- TOC entry 4799 (class 0 OID 32803)
-- Dependencies: 217
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.items OVERRIDING SYSTEM VALUE VALUES ('item', 'yarilo', 'mega sigm', 1, '1.png');
INSERT INTO public.items OVERRIDING SYSTEM VALUE VALUES ('item', 'notyarilo', 'fsdfsdf', 2, '2.png');


--
-- TOC entry 4800 (class 0 OID 32808)
-- Dependencies: 218
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users VALUES ('2da3695b-254d-42c6-a594-a44d70767b4b', 'student');
INSERT INTO public.users VALUES ('843dc127-b46c-4451-8456-2da0a38c4edc', 'student');
INSERT INTO public.users VALUES ('56e8cda6-e7ca-4223-becc-5313aeab9a97', 'student');
INSERT INTO public.users VALUES ('6e4abcca-d37d-4bb2-bf43-e1bb82caad15', 'student');
INSERT INTO public.users VALUES ('857b79a6-56bb-432d-bd8c-d568e5b5c34f', 'student');
INSERT INTO public.users VALUES ('f91f8444-1df1-418f-9dd9-75d041cc1850', 'student');
INSERT INTO public.users VALUES ('78dde412-484a-41b2-b8fc-1fb5a3f3e81e', 'student');
INSERT INTO public.users VALUES ('9b99ebd3-cd49-4660-9370-5a3dd715715e', 'student');
INSERT INTO public.users VALUES ('b023ea31-453e-4f6e-b3c7-047b190f8bae', 'student');
INSERT INTO public.users VALUES ('99f1ee8c-5af4-4b17-9a2c-1707c57f1840', 'student');
INSERT INTO public.users VALUES ('d3d568fc-4f69-46c8-95f9-215f9e5735b6', 'student');
INSERT INTO public.users VALUES ('8d499df0-aef5-43d5-81cd-1c8c37769fa8', 'student');
INSERT INTO public.users VALUES ('dc7a721e-20dc-4c6d-b9c2-086707f840d2', 'student');
INSERT INTO public.users VALUES ('dd256cd1-e5c3-40b6-a005-d03b84f0757a', 'student');
INSERT INTO public.users VALUES ('I', NULL);
INSERT INTO public.users VALUES ('83f39e4a-150b-45a1-b296-185987a6e82b', NULL);
INSERT INTO public.users VALUES ('804cc462-a5d0-408b-9597-246da846ec96', NULL);
INSERT INTO public.users VALUES ('e287350b-6420-4d5f-adf9-f5ba272fa63f', NULL);
INSERT INTO public.users VALUES ('bd5ba217-9124-4726-a1f0-9d6137eed246', NULL);
INSERT INTO public.users VALUES ('bce3aff6-8b44-4782-89b4-5435de81bfb5', NULL);


--
-- TOC entry 4809 (class 0 OID 0)
-- Dependencies: 221
-- Name: inventories_inventory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.inventories_inventory_id_seq', 2, true);


--
-- TOC entry 4810 (class 0 OID 0)
-- Dependencies: 220
-- Name: items_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.items_item_id_seq', 2, true);


--
-- TOC entry 4653 (class 2606 OID 41036)
-- Name: inventories inventories_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.inventories
    ADD CONSTRAINT inventories_pk PRIMARY KEY (inventory_id);


--
-- TOC entry 4651 (class 2606 OID 32841)
-- Name: users users_unique; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_unique UNIQUE (user_uuid);


-- Completed on 2026-01-14 23:05:19

--
-- PostgreSQL database dump complete
--


PGDMP                     	    w           postgres    11.5 (Debian 11.5-1.pgdg90+1)    12.0     L           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            M           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            N           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            O           1262    13067    postgres    DATABASE     x   CREATE DATABASE postgres WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';
    DROP DATABASE postgres;
                postgres    false            P           0    0    DATABASE postgres    COMMENT     N   COMMENT ON DATABASE postgres IS 'default administrative connection database';
                   postgres    false    2895            �            1259    16386    Action    TABLE     P   CREATE TABLE public."Action" (
    id_action integer NOT NULL,
    name text
);
    DROP TABLE public."Action";
       public            postgres    false            �            1259    16384    Action_id_seq    SEQUENCE     �   CREATE SEQUENCE public."Action_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public."Action_id_seq";
       public          postgres    false    197            Q           0    0    Action_id_seq    SEQUENCE OWNED BY     J   ALTER SEQUENCE public."Action_id_seq" OWNED BY public."Action".id_action;
          public          postgres    false    196            �            1259    16411 
   Has_action    TABLE     t   CREATE TABLE public."Has_action" (
    id_strategy bigint NOT NULL,
    id_action integer NOT NULL,
    xml text
);
     DROP TABLE public."Has_action";
       public            postgres    false            �            1259    16397 	   Strategie    TABLE     o   CREATE TABLE public."Strategie" (
    id_strategie bigint NOT NULL,
    id_action integer,
    "order" text
);
    DROP TABLE public."Strategie";
       public            postgres    false            �            1259    16395    Strategie_id_strategie_seq    SEQUENCE     �   CREATE SEQUENCE public."Strategie_id_strategie_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public."Strategie_id_strategie_seq";
       public          postgres    false    199            R           0    0    Strategie_id_strategie_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public."Strategie_id_strategie_seq" OWNED BY public."Strategie".id_strategie;
          public          postgres    false    198            �
           2604    16389    Action id_action    DEFAULT     q   ALTER TABLE ONLY public."Action" ALTER COLUMN id_action SET DEFAULT nextval('public."Action_id_seq"'::regclass);
 A   ALTER TABLE public."Action" ALTER COLUMN id_action DROP DEFAULT;
       public          postgres    false    197    196    197            �
           2604    16400    Strategie id_strategie    DEFAULT     �   ALTER TABLE ONLY public."Strategie" ALTER COLUMN id_strategie SET DEFAULT nextval('public."Strategie_id_strategie_seq"'::regclass);
 G   ALTER TABLE public."Strategie" ALTER COLUMN id_strategie DROP DEFAULT;
       public          postgres    false    198    199    199            F          0    16386    Action 
   TABLE DATA           3   COPY public."Action" (id_action, name) FROM stdin;
    public          postgres    false    197   G       I          0    16411 
   Has_action 
   TABLE DATA           C   COPY public."Has_action" (id_strategy, id_action, xml) FROM stdin;
    public          postgres    false    200   �       H          0    16397 	   Strategie 
   TABLE DATA           G   COPY public."Strategie" (id_strategie, id_action, "order") FROM stdin;
    public          postgres    false    199   �       S           0    0    Action_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public."Action_id_seq"', 4, true);
          public          postgres    false    196            T           0    0    Strategie_id_strategie_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public."Strategie_id_strategie_seq"', 1, false);
          public          postgres    false    198            �
           2606    16394    Action Action_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Action"
    ADD CONSTRAINT "Action_pkey" PRIMARY KEY (id_action);
 @   ALTER TABLE ONLY public."Action" DROP CONSTRAINT "Action_pkey";
       public            postgres    false    197            �
           2606    16418    Has_action Has_action_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public."Has_action"
    ADD CONSTRAINT "Has_action_pkey" PRIMARY KEY (id_strategy, id_action);
 H   ALTER TABLE ONLY public."Has_action" DROP CONSTRAINT "Has_action_pkey";
       public            postgres    false    200    200            �
           2606    16405    Strategie Strategie_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public."Strategie"
    ADD CONSTRAINT "Strategie_pkey" PRIMARY KEY (id_strategie);
 F   ALTER TABLE ONLY public."Strategie" DROP CONSTRAINT "Strategie_pkey";
       public            postgres    false    199            �
           2606    16406    Strategie fk_id_action->action    FK CONSTRAINT     �   ALTER TABLE ONLY public."Strategie"
    ADD CONSTRAINT "fk_id_action->action" FOREIGN KEY (id_action) REFERENCES public."Action"(id_action);
 L   ALTER TABLE ONLY public."Strategie" DROP CONSTRAINT "fk_id_action->action";
       public          postgres    false    197    2756    199            �
           2606    16424    Has_action fk_id_action->action    FK CONSTRAINT     �   ALTER TABLE ONLY public."Has_action"
    ADD CONSTRAINT "fk_id_action->action" FOREIGN KEY (id_action) REFERENCES public."Action"(id_action);
 M   ALTER TABLE ONLY public."Has_action" DROP CONSTRAINT "fk_id_action->action";
       public          postgres    false    200    197    2756            �
           2606    16419 %   Has_action fk_id_strategie->strategie    FK CONSTRAINT     �   ALTER TABLE ONLY public."Has_action"
    ADD CONSTRAINT "fk_id_strategie->strategie" FOREIGN KEY (id_strategy) REFERENCES public."Strategie"(id_strategie);
 S   ALTER TABLE ONLY public."Has_action" DROP CONSTRAINT "fk_id_strategie->strategie";
       public          postgres    false    199    2758    200            F   1   x�3�̍O��L��2�R�K�rR��@��̼. #7�,�+F��� ��-      I      x������ � �      H      x������ � �     
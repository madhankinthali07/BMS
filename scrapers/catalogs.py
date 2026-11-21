"""
Centralized Theater Catalogs for BookMyShow and District across 13 Andhra Pradesh & Telangana Cities:
1. Visakhapatnam (Vizag)
2. Vijayawada
3. Guntur
4. Tirupati
5. Rajahmundry
6. Nellore
7. Kurnool
8. Hyderabad
9. Warangal
10. Karimnagar
11. Nizamabad
12. Khammam
13. Mahabubnagar

Divided systematically into:
- Single Screens (Iconic standalone cinema halls)
- Mixed / Twin / Complex Screens (Dual screens, shared venues, complex names)
- Multiplexes (PVR, INOX, Cinepolis, Asian, Miraj, etc.)
"""

# ==============================================================================
# BOOKMYSHOW THEATER CATALOG
# ==============================================================================
BMS_THEATER_CATALOG = {
    # --------------------------------------------------------------------------
    # 1. VISAKHAPATNAM (VIZAG)
    # --------------------------------------------------------------------------
    "vizag": [
        # Single Screens
        {
            "name": "Sri Melody HDR Dolby Atmos: Vizag",
            "slug": "sri-melody-hdr-dolby-atmos-vizag",
            "venue_code": "MELD",
            "city_slug": "vizag-visakhapatnam",
            "address": "Suryabagh, Jagadamba Junction, V Max Theatre, Vizag 530020",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/sri-melody-hdr-dolby-atmos-vizag/buytickets/MELD"
        },
        {
            "name": "Sri Venkateswara Theatre: Kurmannapalem, Vizag",
            "slug": "sri-venkateswara-theatre-kurmannapalem",
            "venue_code": "SVKV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Kurmannapalem, Gajuwaka, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/sri-venkateswara-theatre-kurmannapalem/buytickets/SVKV"
        },
        {
            "name": "Ramakrishna 70mm: Maddilapalem, Vizag",
            "slug": "ramakrishna-70mm-maddilapalem",
            "venue_code": "RKMV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Opposite AU Campus, Maddilapalem, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/ramakrishna-70mm-maddilapalem/buytickets/RKMV"
        },
        {
            "name": "Laxmi 70mm: Kancharapalem, Vizag",
            "slug": "laxmi-70mm-kancharapalem",
            "venue_code": "LXKV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Kancharapalem Main Road, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/laxmi-70mm-kancharapalem/buytickets/LXKV"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "Sarat Theatre: A/C 4K Laser Dolby Atmos, Vizag",
            "slug": "sarat-theatre-a-c-4k-laser-dolby-atmos-vizag",
            "venue_code": "STTR",
            "city_slug": "vizag-visakhapatnam",
            "address": "Railway Station Road, Dondaparthy, Dwaraka Nagar, Vizag 530016",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/sarat-theatre-a-c-4k-laser-dolby-atmos-vizag/buytickets/STTR"
        },
        {
            "name": "Sangam Theatre: 4K Dolby Atmos, Vizag",
            "slug": "sangam-theatre-4k-dolby-atmos-vizag",
            "venue_code": "SNGV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Railway Station Road, Dondaparthy, Dwaraka Nagar, Vizag 530016",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/sangam-theatre-4k-dolby-atmos-vizag/buytickets/SNGV"
        },
        {
            "name": "Kameswari A/C 70mm: RTC Complex Road, Vizag",
            "slug": "kameswari-ac-70mm",
            "venue_code": "KAMV",
            "city_slug": "vizag-visakhapatnam",
            "address": "RTC Complex Road, Dwaraka Nagar, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/kameswari-ac-70mm/buytickets/KAMV"
        },
        {
            "name": "Kinnera 4K Atmos: RTC Complex Road, Vizag",
            "slug": "kinnera-4k-atmos-vizag",
            "venue_code": "KINV",
            "city_slug": "vizag-visakhapatnam",
            "address": "RTC Complex Road, Dwaraka Nagar, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/kinnera-4k-atmos-vizag/buytickets/KINV"
        },
        {
            "name": "V Max Multiplex Screen 1: Rama Talkies, Vizag",
            "slug": "v-max-multiplex-screen-1",
            "venue_code": "VMXV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Rama Talkies Road, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/v-max-multiplex-screen-1/buytickets/VMXV"
        },
        {
            "name": "V Max Multiplex Screen 2: Rama Talkies, Vizag",
            "slug": "v-max-multiplex-screen-2",
            "venue_code": "VMX2",
            "city_slug": "vizag-visakhapatnam",
            "address": "Rama Talkies Road, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/v-max-multiplex-screen-2/buytickets/VMX2"
        },
        {
            "name": "Jagadamba 70mm Multiplex: 4K Laser Dolby Atmos, Vizag",
            "slug": "jagadamba-70mm-4k-laser-dolby-atmos",
            "venue_code": "JAGV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Jagadamba Centre, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/jagadamba-70mm-4k-laser-dolby-atmos/buytickets/JAGV"
        },
        # Multiplexes
        {
            "name": "INOX: Varun Beach, Beach Road, Vizag",
            "slug": "inox-varun-beach-beach-road",
            "venue_code": "VBMV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Beach Road, Pandurangapuram, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/inox-varun-beach-beach-road/buytickets/VBMV"
        },
        {
            "name": "INOX: CMR Central, Maddilapalem, Vizag",
            "slug": "inox-cmr-central-maddilapalem",
            "venue_code": "CMRV",
            "city_slug": "vizag-visakhapatnam",
            "address": "CMR Central Mall, Maddilapalem, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/inox-cmr-central-maddilapalem/buytickets/CMRV"
        },
        {
            "name": "Cinepolis: Sreekanya, Gajuwaka, Vizag",
            "slug": "cinepolis-sreekanya-gajuwaka",
            "venue_code": "SKGV",
            "city_slug": "vizag-visakhapatnam",
            "address": "Old Gajuwaka Junction, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/cinepolis-sreekanya-gajuwaka/buytickets/SKGV"
        },
        {
            "name": "STBL Cine World Multiplex: Sheela Nagar, Vizag",
            "slug": "stbl-cine-world-multiplex",
            "venue_code": "STBV",
            "city_slug": "vizag-visakhapatnam",
            "address": "BHPV Post, Sheela Nagar, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/stbl-cine-world-multiplex/buytickets/STBV"
        },
        {
            "name": "Mukta A2 Cinemas: Central Mall, Suryabagh, Vizag",
            "slug": "mukta-a2-cinemas-central-mall",
            "venue_code": "MA2V",
            "city_slug": "vizag-visakhapatnam",
            "address": "Suryabagh, Jagadamba Centre, Visakhapatnam",
            "bms_url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/mukta-a2-cinemas-central-mall/buytickets/MA2V"
        }
    ],

    # --------------------------------------------------------------------------
    # 2. VIJAYAWADA
    # --------------------------------------------------------------------------
    "vijayawada": [
        # Single Screens
        {
            "name": "Vijayalakshmi Theater A/C 4K Dolby: Kanuru",
            "slug": "vijayalakshmi-theater-a-c-4k-dolby-kanuru",
            "venue_code": "VIJK",
            "city_slug": "vijayawada",
            "address": "7-30, Kanuru Main Road, Ashok Nagar, Near Kanuru Dhaaba, Vijayawada, Andhra Pradesh 520007, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/vijayalakshmi-theater-a-c-4k-dolby-kanuru/buytickets/VIJK"
        },
        {
            "name": "Sailaja Theatre: Vijayawada",
            "slug": "sailaja-theatre-vijayawada",
            "venue_code": "SVLJ",
            "city_slug": "vijayawada",
            "address": "Andhra Ratna Road, Gandhi Nagar, Opposite Ramakrishna Mission, Vijayawada, Andhra Pradesh 520003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/sailaja-theatre-vijayawada/buytickets/SVLJ"
        },
        {
            "name": "Swarna Cinemax 2K Laser 7.1 Surround:Ibrahimpatnam",
            "slug": "swarna-cinemax-2k-laser-7-1-surround-ibrahimpatnam",
            "venue_code": "SWRN",
            "city_slug": "vijayawada",
            "address": "NH 65, Ring Centre, Ibrahimpatnam, Vijayawada, Andhra Pradesh 521456, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/swarna-cinemax-2k-laser-7-1-surround-ibrahimpatnam/buytickets/SWRN"
        },
        {
            "name": "Swathi Theater: Bhavanipuram (Newly Renovated)",
            "slug": "swathi-theater-bhavanipuram-newly-renovated",
            "venue_code": "SWTH",
            "city_slug": "vijayawada",
            "address": "Bhavanipuram Housing Board Road, Bhavanipuram, V D Puram, Beside Ameenuddin Dhargah, Vijayawada, Andhra Pradesh 520012, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/swathi-theater-bhavanipuram-newly-renovated/buytickets/SWTH"
        },
        {
            "name": "Sairam Screens A/C Dolby 7.1 Surround: Vijayawada",
            "slug": "sairam-screens-a-c-dolby-7-1-surround-vijayawada",
            "venue_code": "STHV",
            "city_slug": "vijayawada",
            "address": "Milk Factory Road, Fraserpeta, Vijayawada, Andhra Pradesh 520001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/sairam-screens-a-c-dolby-7-1-surround-vijayawada/buytickets/STHV"
        },
        {
            "name": "Alankar A/C 4K Dolby Surround: Vijayawada",
            "slug": "alankar-a-c-4k-dolby-surround-vijayawada",
            "venue_code": "ATVJ",
            "city_slug": "vijayawada",
            "address": "Samba Murthy Road, Gandhi Nagar, Near Ramakrishna Mission Ashrama, Vijayawada, Andhra Pradesh 520003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/alankar-a-c-4k-dolby-surround-vijayawada/buytickets/ATVJ"
        },
        {
            "name": "Balaji Cine Villa A/C 2K Laser: Poranki,Vijayawada",
            "slug": "balaji-cine-villa-a-c-2k-laser-poranki-vijayawada",
            "venue_code": "BLJI",
            "city_slug": "vijayawada",
            "address": "Bundar Road, Poranki, Near Priya Foods, Vijayawada, Andhra Pradesh 521137, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/balaji-cine-villa-a-c-2k-laser-poranki-vijayawada/buytickets/BLJI"
        },
        {
            "name": "Jayram Theatre A/c 2K Dolby Digital: Vijayawada",
            "slug": "jayram-theatre-a-c-2k-dolby-digital-vijayawada",
            "venue_code": "JATV",
            "city_slug": "vijayawada",
            "address": "Gandhi Nagar, Samba Murty Road, Andhra Pradesh, Vijayawada, Andhra Pradesh 520003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/jayram-theatre-a-c-2k-dolby-digital-vijayawada/buytickets/JATV"
        },
        {
            "name": "Apsara Cinema House: Vijayawada",
            "slug": "apsara-cinema-house-vijayawada",
            "venue_code": "ACHV",
            "city_slug": "vijayawada",
            "address": "Governor Peta, Eluru Road, Opposite Swarna Mutiplex, Vijayawada, Andhra Pradesh 520002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/apsara-cinema-house-vijayawada/buytickets/ACHV"
        },
        {
            "name": "Tara Screens 2K A/C, Payakapuram: Vijayawada",
            "slug": "tara-screens-2k-a-c-payakapuram-vijayawada",
            "venue_code": "TVRA",
            "city_slug": "vijayawada",
            "address": "D.No.77-16/1-43, Nunna Road, Pipula Road, PNT Colony, Vijayawada, Andhra Pradesh 520015, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/tara-screens-2k-a-c-payakapuram-vijayawada/buytickets/TVRA"
        },
        {
            "name": "Sowmya Theater (Newly Renovated): Vijayawada",
            "slug": "sowmya-theater-newly-renovated-vijayawada",
            "venue_code": "SWOT",
            "city_slug": "vijayawada",
            "address": "5-6-59/26G, Lambadi Pet, Rajeevsarma Nagar, Chittinagar, New colony, Vijayawada, Andhra Pradesh 520001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/sowmya-theater-newly-renovated-vijayawada/buytickets/SWOT"
        },
        {
            "name": "Balaji Iconia A/C 2K Laser Dolby 7.1:Ibrahimpatnam",
            "slug": "balaji-iconia-a-c-2k-laser-dolby-7-1-ibrahimpatnam",
            "venue_code": "BDMA",
            "city_slug": "vijayawada",
            "address": "NH 65, Ibrahimpatnam, Vijayawada, Andhra Pradesh 521456, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/balaji-iconia-a-c-2k-laser-dolby-7-1-ibrahimpatnam/buytickets/BDMA"
        },
        {
            "name": "Navarang Theatre: Vijayawada",
            "slug": "navarang-theatre-vijayawada",
            "venue_code": "NVRN",
            "city_slug": "vijayawada",
            "address": "Buckinghampeta, Palaparthi Vari Street, Near Help Hospitals, Vijayawada, Andhra Pradesh 520002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/navarang-theatre-vijayawada/buytickets/NVRN"
        },
        {
            "name": "Sri Vijaya Lakshmi Theater: Kankipadu",
            "slug": "sri-vijaya-lakshmi-theater-kankipadu",
            "venue_code": "SVLA",
            "city_slug": "vijayawada",
            "address": "CQP7+VG8, Vijayawada - Machilipatnam Road, Kankipadu, Andhra Pradesh 521151, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/sri-vijaya-lakshmi-theater-kankipadu/buytickets/SVLA"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "INOX: Urvasi Complex, Gandhi Nagar",
            "slug": "inox-urvasi-complex-gandhi-nagar",
            "venue_code": "INVJ",
            "city_slug": "vijayawada",
            "address": "Urvashi Theatre Complex, 26-2-66/A, Andhra Ratna Road, Gandhi Nagar, Vijayawada, Andhra Pradesh 520003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/inox-urvasi-complex-gandhi-nagar/buytickets/INVJ"
        },
        {
            "name": "G3 Theatres: Raj Yuvraj, Vijayawada",
            "slug": "g3-theatres-raj-yuvraj-vijayawada",
            "venue_code": "MGGG",
            "city_slug": "vijayawada",
            "address": "Andhra Ratna Road, Gandhi Nagar, Vijayawada, Andhra Pradesh 520003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/g3-theatres-raj-yuvraj-vijayawada/buytickets/MGGG"
        },
        # Multiplexes
        {
            "name": "Capital Cinemas: Trendset Mall, Vijayawada",
            "slug": "capital-cinemas-trendset-mall-vijayawada",
            "venue_code": "CCTL",
            "city_slug": "vijayawada",
            "address": "Trendset Mall, 40/1/56, MG Road, Sai Nagar, Kala Nagar, Acharya Ranga Nagar, Benz Circle, Vijayawada, Andhra Pradesh 520008, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/capital-cinemas-trendset-mall-vijayawada/buytickets/CCTL"
        },
        {
            "name": "Cinepolis: PVP Square Mall, Vijayawada",
            "slug": "cinepolis-pvp-square-mall-vijayawada",
            "venue_code": "CPVJ",
            "city_slug": "vijayawada",
            "address": "4th Floor, PVP Square Mall, Mahatma Gandhi Road, Labbipet, Mogalrajapuram, Vijayawada, Andhra Pradesh 520010, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/cinepolis-pvp-square-mall-vijayawada/buytickets/CPVJ"
        },
        {
            "name": "ABR Cinemas Neo Screen X:  Kanuru, Vijayawada",
            "slug": "abr-cinemas-neo-screen-x-kanuru-vijayawada",
            "venue_code": "ABCR",
            "city_slug": "vijayawada",
            "address": "Elevate Mall, Pune-Machilipatnam Highway, Kanuru, Vijayawada, Andhra Pradesh 520007, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/abr-cinemas-neo-screen-x-kanuru-vijayawada/buytickets/ABCR"
        },
        {
            "name": "INOX: Laila Mall, 4K LASER, DOLBY ATMOS, M.G Road",
            "slug": "inox-laila-mall-4k-laser-dolby-atmos-m-g-road",
            "venue_code": "LAIM",
            "city_slug": "vijayawada",
            "address": "4th Floor, Laila Mall, M.G. Road, Vijayawada, Andhra Pradesh 520002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/inox-laila-mall-4k-laser-dolby-atmos-m-g-road/buytickets/LAIM"
        },
        {
            "name": "INOX: LEPL Icon, Patamata",
            "slug": "inox-lepl-icon-patamata",
            "venue_code": "INVP",
            "city_slug": "vijayawada",
            "address": "3rd Floor, LEPL Icon, RTC Colony, Benz Circle, Patamata, Near Maris Stella College, Vijayawada, Andhra Pradesh 520010, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/inox-lepl-icon-patamata/buytickets/INVP"
        },
        {
            "name": "Cinepolis: Power One Mall, Vijayawada",
            "slug": "cinepolis-power-one-mall-vijayawada",
            "venue_code": "CPOV",
            "city_slug": "vijayawada",
            "address": "Cinepolis India Pvt Ltd, 3rd Floor, Power One Mall, Survery no -220/4 Kanuru gram, Bunder Road, District- Krishna, Vijayawada, Andhra Pradesh 520007, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/cinepolis-power-one-mall-vijayawada/buytickets/CPOV"
        },
        {
            "name": "Ram Cinemas: Gunadala A/C 4K Digital DOLBY ATMOS",
            "slug": "ram-cinemas-gunadala-a-c-4k-digital-dolby-atmos",
            "venue_code": "RMTV",
            "city_slug": "vijayawada",
            "address": "St. Joseph Complex, Eluru Road, Near Andhra Bank Gunadala Branch, Vijayawada, Andhra Pradesh 520004, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/ram-cinemas-gunadala-a-c-4k-digital-dolby-atmos/buytickets/RMTV"
        },
        {
            "name": "Swarna Multiplex: Vijayawada",
            "slug": "swarna-multiplex-vijayawada",
            "venue_code": "JTSC",
            "city_slug": "vijayawada",
            "address": "Swarnalok Complex, Eluru Rd, Governorpet, Vijayawada, Andhra Pradesh 520002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/swarna-multiplex-vijayawada/buytickets/JTSC"
        },
        {
            "name": "PVR: Ripples, Vijayawada",
            "slug": "pvr-ripples-vijayawada",
            "venue_code": "PRSV",
            "city_slug": "vijayawada",
            "address": "Mahatma Gandhi Road, Labbipet, Telaprolu, Andhra Pradesh 520010, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/pvr-ripples-vijayawada/buytickets/PRSV"
        },
        {
            "name": "Ravindra Cinemas: Vijayawada",
            "slug": "ravindra-cinemas-vijayawada",
            "venue_code": "RCVD",
            "city_slug": "vijayawada",
            "address": "Singh Nagar, Laxminagar, Nunna Road, Kandrika, Payakapuram, Vijayawada, Andhra Pradesh 520015, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/ravindra-cinemas-vijayawada/buytickets/RCVD"
        },
        {
            "name": "Sivakrishna Cinemas A/C 2K DTS: Kondapalli",
            "slug": "sivakrishna-cinemas-a-c-2k-dts-kondapalli",
            "venue_code": "SIKC",
            "city_slug": "vijayawada",
            "address": "D.No. 32-239, Mylavaram Road, NH 30, Kondapalli, Ibrahimpatnam, Vijayawada, Andhra Pradesh 521228, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/sivakrishna-cinemas-a-c-2k-dts-kondapalli/buytickets/SIKC"
        },
        {
            "name": "Venkata Krishna Luxury Cinemas: Poranki",
            "slug": "venkata-krishna-luxury-cinemas-poranki",
            "venue_code": "VAKR",
            "city_slug": "vijayawada",
            "address": "Sitapuram Colony, NH 65, Poranki, Near ICICI Bank, Vijayawada, Andhra Pradesh 521137, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/venkata-krishna-luxury-cinemas-poranki/buytickets/VAKR"
        },
        {
            "name": "Sri Ramachandra Cinemas: Kankipadu",
            "slug": "sri-ramachandra-cinemas-kankipadu",
            "venue_code": "SRCZ",
            "city_slug": "vijayawada",
            "address": "Royyuru Kankipadu Road, Opposite Kankipadu Panchayati Office, Kankipadu, Andhra Pradesh 521151, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/vijayawada/sri-ramachandra-cinemas-kankipadu/buytickets/SRCZ"
        }
    ],

    # --------------------------------------------------------------------------
    # 3. GUNTUR
    # --------------------------------------------------------------------------
    "guntur": [
        # Single Screens
        {
            "name": "Cine Prime: Guntur",
            "slug": "cine-prime-guntur",
            "venue_code": "CNPR",
            "city_slug": "guntur",
            "address": "Nagarjuna Sagar Road, Srinivasarao Pet, Guntur, Andhra Pradesh 522003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/cine-prime-guntur/buytickets/CNPR"
        },
        {
            "name": "Cine Square Dolby Atmos A/C: Guntur",
            "slug": "cine-square-dolby-atmos-a-c-guntur",
            "venue_code": "CSER",
            "city_slug": "guntur",
            "address": "Amravati Road, Gorantla, Near Gorantla Electricity Office, Guntur, Andhra Pradesh 522034, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/cine-square-dolby-atmos-a-c-guntur/buytickets/CSER"
        },
        {
            "name": "Sreemanth Mahal: Chebrolu",
            "slug": "sreemanth-mahal-chebrolu",
            "venue_code": "SRMH",
            "city_slug": "guntur",
            "address": "Guntur - Ponnur Road, Opposite Essar Petrol Bunk, Chebrolu, Andhra Pradesh 522212, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/sreemanth-mahal-chebrolu/buytickets/SRMH"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "Hollywood Bollywood Theaters: Guntur",
            "slug": "hollywood-bollywood-theaters-guntur",
            "venue_code": "HLWD",
            "city_slug": "guntur",
            "address": "Lakshmipuram Main Road, Brodipet, Guntur, Andhra Pradesh 522002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/hollywood-bollywood-theaters-guntur/buytickets/HLWD"
        },
        # Multiplexes
        {
            "name": "Studio 81 Cinemas: 4K Laser Dolby Atmos, Guntur",
            "slug": "studio-81-cinemas-4k-laser-dolby-atmos-guntur",
            "venue_code": "STTY",
            "city_slug": "guntur",
            "address": "KSP Prime Mall, Opposite Gunta Ground, Near D Mart, Guntur, Andhra Pradesh 522001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/studio-81-cinemas-4k-laser-dolby-atmos-guntur/buytickets/STTY"
        },
        {
            "name": "Harihar Cinemas: Guntur",
            "slug": "harihar-cinemas-guntur",
            "venue_code": "HHCG",
            "city_slug": "guntur",
            "address": "Opp LVR Club, Road Lakshmipuram, Koritepadu Road, Guntur, Andhra Pradesh 522007, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/harihar-cinemas-guntur/buytickets/HHCG"
        },
        {
            "name": "Siva Cinemas 4K Dolby Atmos: Guntur",
            "slug": "siva-cinemas-4k-dolby-atmos-guntur",
            "venue_code": "SCAG",
            "city_slug": "guntur",
            "address": "17th Lane, Arundelpet, Guntur, Andhra Pradesh 522002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/guntur/siva-cinemas-4k-dolby-atmos-guntur/buytickets/SCAG"
        }
    ],

    # --------------------------------------------------------------------------
    # 4. TIRUPATI
    # --------------------------------------------------------------------------
    "tirupati": [
        # Single Screens
        {
            "name": "NVR Jaysyam A/C 4K Dolby Atmos: Tirupati",
            "slug": "nvr-jaysyam-a-c-4k-dolby-atmos-tirupati",
            "venue_code": "JAYD",
            "city_slug": "tirupati",
            "address": "Mallaiah Gunta Katta, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/nvr-jaysyam-a-c-4k-dolby-atmos-tirupati/buytickets/JAYD"
        },
        {
            "name": "NVR Sandhya Theater 4K Dolby Atmos: Tirupati",
            "slug": "nvr-sandhya-theater-4k-dolby-atmos-tirupati",
            "venue_code": "STDA",
            "city_slug": "tirupati",
            "address": "13-6-751, Jayasam Road, Mallaiah Gunta Katta, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/nvr-sandhya-theater-4k-dolby-atmos-tirupati/buytickets/STDA"
        },
        {
            "name": "KrishnaTeja A/C 4K Dolby(Newly Renovated):Tirupati",
            "slug": "krishnateja-a-c-4k-dolby-newly-renovated-tirupati",
            "venue_code": "KRTT",
            "city_slug": "tirupati",
            "address": "Jayasam Road, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/krishnateja-a-c-4k-dolby-newly-renovated-tirupati/buytickets/KRTT"
        },
        {
            "name": "Padma Picture Palace A/C 4K Dolby Atmos: Renigunta",
            "slug": "padma-picture-palace-a-c-4k-dolby-atmos-renigunta",
            "venue_code": "PPPD",
            "city_slug": "tirupati",
            "address": "Gowri Nagar, GM Street, Tirupati, Andhra Pradesh 517520, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/padma-picture-palace-a-c-4k-dolby-atmos-renigunta/buytickets/PPPD"
        },
        {
            "name": "Pratap Theater A/c 4K Dolby Atmos: Tirupati",
            "slug": "pratap-theater-a-c-4k-dolby-atmos-tirupati",
            "venue_code": "PTDT",
            "city_slug": "tirupati",
            "address": "Jayasam Road, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/pratap-theater-a-c-4k-dolby-atmos-tirupati/buytickets/PTDT"
        },
        {
            "name": "NVR Velrams A/c 4K Dolby Surround: Tirupati",
            "slug": "nvr-velrams-a-c-4k-dolby-surround-tirupati",
            "venue_code": "VELR",
            "city_slug": "tirupati",
            "address": "Mallaiah Gunta Katta, Jayasam Road, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/nvr-velrams-a-c-4k-dolby-surround-tirupati/buytickets/VELR"
        },
        {
            "name": "Pratap Delux A/c 2k Dolby Atmos: Tirupati",
            "slug": "pratap-delux-a-c-2k-dolby-atmos-tirupati",
            "venue_code": "MPTT",
            "city_slug": "tirupati",
            "address": "Jayasam Road, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/pratap-delux-a-c-2k-dolby-atmos-tirupati/buytickets/MPTT"
        },
        {
            "name": "CVS Movie Land A/c DTS: Tirupati",
            "slug": "cvs-movie-land-a-c-dts-tirupati",
            "venue_code": "CVTT",
            "city_slug": "tirupati",
            "address": "Jayasam Road, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/cvs-movie-land-a-c-dts-tirupati/buytickets/CVTT"
        },
        {
            "name": "Srinivas Teja A/C DTS: Tirupati",
            "slug": "srinivas-teja-a-c-dts-tirupati",
            "venue_code": "STDT",
            "city_slug": "tirupati",
            "address": "Jayasam Road, Tata Nagar, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/srinivas-teja-a-c-dts-tirupati/buytickets/STDT"
        },
        # Multiplexes
        {
            "name": "PGR Cinemas A/C 4K Dolby Atmos: Tirupati",
            "slug": "pgr-cinemas-a-c-4k-dolby-atmos-tirupati",
            "venue_code": "PGRC",
            "city_slug": "tirupati",
            "address": "Tata Nagar, Near Mahatma Gandhi Junction, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/pgr-cinemas-a-c-4k-dolby-atmos-tirupati/buytickets/PGRC"
        },
        {
            "name": "CS Cinemas (Devendra Theater) A/C 4K Dolby Atmos",
            "slug": "cs-cinemas-devendra-theater-a-c-4k-dolby-atmos",
            "venue_code": "CSCT",
            "city_slug": "tirupati",
            "address": "RS Gardens, Leela Mahal Road, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/cs-cinemas-devendra-theater-a-c-4k-dolby-atmos/buytickets/CSCT"
        },
        {
            "name": "Palani Cinemas A/C 7.1 Dolby Digital: Tirupati",
            "slug": "palani-cinemas-a-c-7-1-dolby-digital-tirupati",
            "venue_code": "PTTI",
            "city_slug": "tirupati",
            "address": "Royal Nagar, Rayala Cheruvuru Road, Nearby Krishna Temple, Tirupati, Andhra Pradesh 517501, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/palani-cinemas-a-c-7-1-dolby-digital-tirupati/buytickets/PTTI"
        },
        {
            "name": "SV Cinemas(Ambica) A/C 4K Dolby Atmos: Chandragiri",
            "slug": "sv-cinemas-ambica-a-c-4k-dolby-atmos-chandragiri",
            "venue_code": "TRSV",
            "city_slug": "tirupati",
            "address": "Tirupati Road, Reddivaripalle, Near Chandragiri Bus Stop, Tirupati, Andhra Pradesh 517101, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/tirupati/sv-cinemas-ambica-a-c-4k-dolby-atmos-chandragiri/buytickets/TRSV"
        }
    ],

    # --------------------------------------------------------------------------
    # 5. RAJAHMUNDRY
    # --------------------------------------------------------------------------
    "rajahmundry": [
        # Single Screens
        {
            "name": "Apsara Laser R.G.B 4K Dolby Atmos: Rajahmundry",
            "slug": "apsara-laser-r-g-b-4k-dolby-atmos-rajahmundry",
            "venue_code": "GATR",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Syamalamba Temple Road, Mangalavaripeta, Near Sri Vinayaka Temple, Rajahmundry, Andhra Pradesh 533101, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/apsara-laser-r-g-b-4k-dolby-atmos-rajahmundry/buytickets/GATR"
        },
        {
            "name": "Swamy Theatre LASER 4K DOLBY: Rajahmundry",
            "slug": "swamy-theatre-laser-4k-dolby-rajahmundry",
            "venue_code": "SYTR",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Annapurnamma peta, Near Rajahmundry Traffic Police Station, Rajahmundry, Andhra Pradesh 533101, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/swamy-theatre-laser-4k-dolby-rajahmundry/buytickets/SYTR"
        },
        {
            "name": "Yuvaraj Screens Dolby Atmos: Kovvur",
            "slug": "yuvaraj-screens-dolby-atmos-kovvur",
            "venue_code": "YSDK",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Mini, Rajendra St, Kovvur, Rajamahendravaram (Rajahmundry), Andhra Pradesh 534350, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/yuvaraj-screens-dolby-atmos-kovvur/buytickets/YSDK"
        },
        {
            "name": "VS Mahal 4k Dolby Atmos 3D: Namavaram",
            "slug": "vs-mahal-4k-dolby-atmos-3d-namavaram",
            "venue_code": "VSMH",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Satilite City Namavaram, A- Block, Namavaram - Moorapudi Road, Rajahmundry, Andhra Pradesh 533107, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/vs-mahal-4k-dolby-atmos-3d-namavaram/buytickets/VSMH"
        },
        {
            "name": "Sri Sivajyothi 2K Cinema 7.1 Dolby: Rajahmundry",
            "slug": "sri-sivajyothi-2k-cinema-7-1-dolby-rajahmundry",
            "venue_code": "SSJR",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Seshayya Metta, Near Shreesaidarbaar Sai Temple, Rajahmundry, Andhra Pradesh 533101, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/sri-sivajyothi-2k-cinema-7-1-dolby-rajahmundry/buytickets/SSJR"
        },
        {
            "name": "Sri Venkata Surya Palace 4K Dolby Atmos: Kadiam",
            "slug": "sri-venkata-surya-palace-4k-dolby-atmos-kadiam",
            "venue_code": "SVSM",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Kadiyam, Kadiyam Mandal, Near Shirdi Sai Convent, Rajahmundry, Andhra Pradesh 533103, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/sri-venkata-surya-palace-4k-dolby-atmos-kadiam/buytickets/SVSM"
        },
        {
            "name": "Murali Krishna Cinema A/C 4K: Dowlaiswaram",
            "slug": "murali-krishna-cinema-a-c-4k-dowlaiswaram",
            "venue_code": "MUDT",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "SH 41, VGTPS Colony, Near Dowlaiswaram Bus Stand, Dowlaiswaram, Andhra Pradesh 533125, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/murali-krishna-cinema-a-c-4k-dowlaiswaram/buytickets/MUDT"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "Surya Complex Laser RGB 4K Dolby Atmos:Rajahmundry",
            "slug": "surya-complex-laser-rgb-4k-dolby-atmos-rajahmundry",
            "venue_code": "SRYR",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Lakshmivarapu Pet, Seshayya Metta, Near Sub Collector`s Office, Behind Police Guest House, Rajahmundry, Andhra Pradesh 533103, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/surya-complex-laser-rgb-4k-dolby-atmos-rajahmundry/buytickets/SRYR"
        },
        # Multiplexes
        {
            "name": "Sarathi Cinemas(Prasaditya Mall):Rajamahendravaram",
            "slug": "sarathi-cinemas-prasaditya-mall-rajamahendravaram",
            "venue_code": "SCPI",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Prasad Aditya Mall, F1, Anala Venkatappa Rao Road, Venkateswara Nagar, Opposite GAIL, Rajamahendravaram (Rajahmundry), Andhra Pradesh 533103, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/sarathi-cinemas-prasaditya-mall-rajamahendravaram/buytickets/SCPI"
        },
        {
            "name": "Sri Sai Krishna 2K (Anusri Cinemas): Rajahmundry",
            "slug": "sri-sai-krishna-2k-anusri-cinemas-rajahmundry",
            "venue_code": "SKRJ",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Syamalamba Temple Road, SH 41, Mangalavaripeta, Rajamahendravaram (Rajahmundry), Andhra Pradesh 533101, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/sri-sai-krishna-2k-anusri-cinemas-rajahmundry/buytickets/SKRJ"
        },
        {
            "name": "Fortune Four Cinemas A/C 2K 7.1: Rajanagaram",
            "slug": "fortune-four-cinemas-a-c-2k-7-1-rajanagaram",
            "venue_code": "RUCM",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "Rajanagaram Main Road, Near Sai Baba Temple, Opposite TTD Kalyana Mandapam, Rajahmundry, Andhra Pradesh 533294, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/fortune-four-cinemas-a-c-2k-7-1-rajanagaram/buytickets/RUCM"
        },
        {
            "name": "Akshara Cinemas Dolby Atmos: Ravulapalem",
            "slug": "akshara-cinemas-dolby-atmos-ravulapalem",
            "venue_code": "AKSR",
            "city_slug": "rajamahendravaram-rajahmundry",
            "address": "National Highway 16, Near - Gayatri Mobiles, Ravulapalem, Andhra Pradesh 533238, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/rajamahendravaram-rajahmundry/akshara-cinemas-dolby-atmos-ravulapalem/buytickets/AKSR"
        }
    ],

    # --------------------------------------------------------------------------
    # 6. NELLORE
    # --------------------------------------------------------------------------
    "nellore": [
        # Single Screens
        {
            "name": "Rain Cinema: Nellore",
            "slug": "rain-cinema-nellore",
            "venue_code": "RACN",
            "city_slug": "nellore",
            "address": "Rain Square, Ambedkar Nagar, Dargamitta, Nellore, Andhra Pradesh 524003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/nellore/rain-cinema-nellore/buytickets/RACN"
        },
        {
            "name": "Jameela Mahal: Buchireddypalem",
            "slug": "jameela-mahal-buchireddypalem",
            "venue_code": "JMBA",
            "city_slug": "nellore",
            "address": "Buchi Old, Bus stand, SH 57, Nagamambapuram, Buchireddypalem, Andhra Pradesh 524305, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/nellore/jameela-mahal-buchireddypalem/buytickets/JMBA"
        },
        # Multiplexes
        {
            "name": "Siri Multiplex: Nellore",
            "slug": "siri-multiplex-nellore",
            "venue_code": "JTSM",
            "city_slug": "nellore",
            "address": "Ramji Nagar, ., Nellore, Andhra Pradesh 524001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/nellore/siri-multiplex-nellore/buytickets/JTSM"
        }
    ],

    # --------------------------------------------------------------------------
    # 7. KURNOOL
    # --------------------------------------------------------------------------
    "kurnool": [
        # Single Screens
        {
            "name": "Vijay Theatre: Joharapuram, Kurnool",
            "slug": "vijay-theatre-joharapuram",
            "venue_code": "VJYK",
            "city_slug": "kurnool",
            "address": "Joharapuram, Kurnool",
            "bms_url": "https://in.bookmyshow.com/cinemas/kurnool/vijay-theatre-joharapuram/buytickets/VJYK"
        },
        {
            "name": "Victory Talkies: Minchin Bazar St, Kurnool",
            "slug": "victory-talkies-minchin-bazar",
            "venue_code": "VTCK",
            "city_slug": "kurnool",
            "address": "Minchin Bazar, Marwari Street, Kurnool",
            "bms_url": "https://in.bookmyshow.com/cinemas/kurnool/victory-talkies-minchin-bazar/buytickets/VTCK"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "Venkatesh Cine Complex: Beside Exhibition Ground",
            "slug": "venkatesh-cine-complex-beside-exhibition-ground",
            "venue_code": "VCCK",
            "city_slug": "kurnool",
            "address": "Beside Exhibition Ground, Kurnool",
            "bms_url": "https://in.bookmyshow.com/cinemas/kurnool/venkatesh-cine-complex-beside-exhibition-ground/buytickets/VCCK"
        },
        {
            "name": "Sri Rama & Sri Krishna Cinemas: Nandikotkur",
            "slug": "sri-rama-sri-krishna-cinemas-nandikotkur",
            "venue_code": "SRKN",
            "city_slug": "kurnool",
            "address": "Nandikotkur Road, Kurnool",
            "bms_url": "https://in.bookmyshow.com/cinemas/kurnool/sri-rama-sri-krishna-cinemas-nandikotkur/buytickets/SRKN"
        },
        # Multiplexes
        {
            "name": "SVC Cinemas: City Square Mall, Kurnool",
            "slug": "svc-cinemas-city-square-mall-kurnool",
            "venue_code": "SVKK",
            "city_slug": "kurnool",
            "address": "City Square Mall, Kurnool",
            "bms_url": "https://in.bookmyshow.com/cinemas/kurnool/svc-cinemas-city-square-mall-kurnool/buytickets/SVKK"
        }
    ],

    # --------------------------------------------------------------------------
    # 8. HYDERABAD
    # --------------------------------------------------------------------------
    "hyderabad": [
        # Single Screens
        {
            "name": "Sree Ramulu 70mm 4K Laser: Moosapet",
            "slug": "sree-ramulu-70mm-4k-laser-moosapet",
            "venue_code": "SRMO",
            "city_slug": "hyderabad",
            "address": "Opp. Laxmikaka and Sashikala Theaters, Bhavani Nagar Moosapet, Near State Bank Of Hyderabad, Hyderabad, Telangana 500018, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sree-ramulu-70mm-4k-laser-moosapet/buytickets/SRMO"
        },
        {
            "name": "MovieMax: AMR, ECIL Secunderabad",
            "slug": "moviemax-amr-ecil-secunderabad",
            "venue_code": "MMAH",
            "city_slug": "hyderabad",
            "address": "AMR Planet Mall,1,Rd,373/1 and 373.3, Trimulgherry, ECIL Road, Extn -  Moula Ali, Secunderabad, Extn - Moula Ali, Secunderabad, Hyderabad, Telangana 500040, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/moviemax-amr-ecil-secunderabad/buytickets/MMAH"
        },
        {
            "name": "Sai Ranga70MM 4KLaser Dolby7.1 AirCooled: Miyapur",
            "slug": "sai-ranga70mm-4klaser-dolby7-1-aircooled-miyapur",
            "venue_code": "SRCM",
            "city_slug": "hyderabad",
            "address": "No 1-138/1,Plot No P-4 to 88, Madhava Nagar Colony, Miyapur, Near Shilpa Nursing Home, Hyderabad, Telangana 500049, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sai-ranga70mm-4klaser-dolby7-1-aircooled-miyapur/buytickets/SRCM"
        },
        {
            "name": "Gokul 70MM 4K DTS: Erragadda",
            "slug": "gokul-70mm-4k-dts-erragadda",
            "venue_code": "GOKU",
            "city_slug": "hyderabad",
            "address": "Main Road, Vikaspuri, Erragadda, Beside Nexa Maruthi Showroom, Hyderabad, Telangana 500018, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/gokul-70mm-4k-dts-erragadda/buytickets/GOKU"
        },
        {
            "name": "Sandhya 70MM 4K Dolby Atmos: RTC X Roads",
            "slug": "sandhya-70mm-4k-dolby-atmos-rtc-x-roads",
            "venue_code": "SMMR",
            "city_slug": "hyderabad",
            "address": "RTC X Roads, Jawahar Nagar, Opposite Bawarchi Restaurant, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sandhya-70mm-4k-dolby-atmos-rtc-x-roads/buytickets/SMMR"
        },
        {
            "name": "Sri Sai Ram 70mm A/C 4k Laser Dolby 7.1:Malkajgiri",
            "slug": "sri-sai-ram-70mm-a-c-4k-laser-dolby-7-1-malkajgiri",
            "venue_code": "SSRM",
            "city_slug": "hyderabad",
            "address": "Yadav Nagar, West Malkajgiri, Secunderabad, Hyderabad, Telangana 500047, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sri-sai-ram-70mm-a-c-4k-laser-dolby-7-1-malkajgiri/buytickets/SSRM"
        },
        {
            "name": "Arjun 70MM: Kukatpally",
            "slug": "arjun-70mm-kukatpally",
            "venue_code": "ARJU",
            "city_slug": "hyderabad",
            "address": "Plot No 2, Sr 178, National Highway 9, Kukatpally, Near KPHB Road, KPHB Phase III, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/arjun-70mm-kukatpally/buytickets/ARJU"
        },
        {
            "name": "Cine Town Indra Nagendra: Karmanghat",
            "slug": "cine-town-indra-nagendra-karmanghat",
            "venue_code": "INKM",
            "city_slug": "hyderabad",
            "address": "10-1-99/7A, Karmanghat Road, Thapovan Colony, Lingojiguda, Saroor Nagar East, Hyderabad, Telangana 500035, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cine-town-indra-nagendra-karmanghat/buytickets/INKM"
        },
        {
            "name": "BR Hitech 70mm: Madhapur",
            "slug": "br-hitech-70mm-madhapur",
            "venue_code": "HMHD",
            "city_slug": "hyderabad",
            "address": "Hitech City Road, Sri Sai Nagar, Madhapur, Near State Bank Of India, Hyderabad, Telangana 500034, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/br-hitech-70mm-madhapur/buytickets/HMHD"
        },
        {
            "name": "Sandhya 35mm 4k Laser & Dolby Atmos: RTC X Roads",
            "slug": "sandhya-35mm-4k-laser-dolby-atmos-rtc-x-roads",
            "venue_code": "SNDY",
            "city_slug": "hyderabad",
            "address": "Musheerabad Main Road, Jawahar Nagar, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sandhya-35mm-4k-laser-dolby-atmos-rtc-x-roads/buytickets/SNDY"
        },
        {
            "name": "Vijetha 70MM 4k Atmos: Borabanda",
            "slug": "vijetha-70mm-4k-atmos-borabanda",
            "venue_code": "VTRB",
            "city_slug": "hyderabad",
            "address": "Snehapuri Colony, Borabanda, Vinayakarao Nagar, Hyderabad, Telangana 500018, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/vijetha-70mm-4k-atmos-borabanda/buytickets/VTRB"
        },
        {
            "name": "Sudarshan 35MM 4k Laser & Dolby Atmos: RTC X Roads",
            "slug": "sudarshan-35mm-4k-laser-dolby-atmos-rtc-x-roads",
            "venue_code": "SUDA",
            "city_slug": "hyderabad",
            "address": "RTC X Roads, Chikkadpally, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sudarshan-35mm-4k-laser-dolby-atmos-rtc-x-roads/buytickets/SUDA"
        },
        {
            "name": "Indra Venkataramana Padmavati Cinema: Kachiguda",
            "slug": "indra-venkataramana-padmavati-cinema-kachiguda",
            "venue_code": "VRKC",
            "city_slug": "hyderabad",
            "address": "Kachiguda Station Road, Parvarish Bagh Colony, Lingampally, Kachiguda, Near IDBI Bank, Hyderabad, Telangana 500027, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/indra-venkataramana-padmavati-cinema-kachiguda/buytickets/VRKC"
        },
        {
            "name": "Devi 70MM 4K Laser & Dolby Atmos: RTC X Roads",
            "slug": "devi-70mm-4k-laser-dolby-atmos-rtc-x-roads",
            "venue_code": "DVRR",
            "city_slug": "hyderabad",
            "address": "RTC Cross Road, Chikkadpally, Himayatnagar, Near Labour Department, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/devi-70mm-4k-laser-dolby-atmos-rtc-x-roads/buytickets/DVRR"
        },
        {
            "name": "UK Cineplex: Nacharam, Hyderabad",
            "slug": "uk-cineplex-nacharam-hyderabad",
            "venue_code": "UKCC",
            "city_slug": "hyderabad",
            "address": "SY No 91 and 156, Nacharam Uppal Mandal,Medchal, Malkajgiri, Hyderabad, Telangana 500076, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/uk-cineplex-nacharam-hyderabad/buytickets/UKCC"
        },
        {
            "name": "VLS Sridevi 2K A/C Dts: Chilakalguda",
            "slug": "vls-sridevi-2k-a-c-dts-chilakalguda",
            "venue_code": "SCHC",
            "city_slug": "hyderabad",
            "address": "Railway Colony, Chilakalguda, Secunderabad, Hyderabad, Telangana 500061, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/vls-sridevi-2k-a-c-dts-chilakalguda/buytickets/SCHC"
        },
        {
            "name": "Vyjayanthi Cinema A/C 2K: Nacharam",
            "slug": "vyjayanthi-cinema-a-c-2k-nacharam",
            "venue_code": "VAJA",
            "city_slug": "hyderabad",
            "address": "New Raghavendra Nagar, Nacharam Mallapur Road, Near Nacharam Bus Stop, Hyderabad, Telangana 500076, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/vyjayanthi-cinema-a-c-2k-nacharam/buytickets/VAJA"
        },
        {
            "name": "Platinum Movietime Cinema: Gachibowli SLN Terminus",
            "slug": "platinum-movietime-cinema-gachibowli-sln-terminus",
            "venue_code": "MTHY",
            "city_slug": "hyderabad",
            "address": "3rd Floor, SLN Terminus, Gachibowli - Miyapur Road, Jayabheri Enclave, Hyderabad, Telangana 500032, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/platinum-movietime-cinema-gachibowli-sln-terminus/buytickets/MTHY"
        },
        {
            "name": "Prashant Cinema: Secunderabad (Newly Renovated)",
            "slug": "prashant-cinema-secunderabad-newly-renovated",
            "venue_code": "PRCS",
            "city_slug": "hyderabad",
            "address": "73, Red Cross Road, Shivaji nagar, Secunderabad, Beside Passport Office, Hyderabad, Telangana 500003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/prashant-cinema-secunderabad-newly-renovated/buytickets/PRCS"
        },
        {
            "name": "Alankar (Pratap Theatre): Langer House",
            "slug": "alankar-pratap-theatre-langer-house",
            "venue_code": "PTTH",
            "city_slug": "hyderabad",
            "address": "9-1-44/2/1-A, Langer Houz, Beside Navabharat Service Station, Hyderabad, Telangana 500008, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/alankar-pratap-theatre-langer-house/buytickets/PTTH"
        },
        {
            "name": "Sushma 2K Dolby Digital Cinema: Vanasthalipuram",
            "slug": "sushma-2k-dolby-digital-cinema-vanasthalipuram",
            "venue_code": "SCVM",
            "city_slug": "hyderabad",
            "address": "Vanasthalipuram, Vijayawada Highway, Near Bharat Gas Industries, Hyderabad, Telangana 500070, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sushma-2k-dolby-digital-cinema-vanasthalipuram/buytickets/SCVM"
        },
        {
            "name": "Rama Krishna 70mm: Abids",
            "slug": "rama-krishna-70mm-abids",
            "venue_code": "RKMH",
            "city_slug": "hyderabad",
            "address": "Troop Bazar Main Road, Troop Bazaar, Koti, Hyderabad, Telangana 500001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/rama-krishna-70mm-abids/buytickets/RKMH"
        },
        {
            "name": "Bhujanga 70MM: Jeedimetla",
            "slug": "bhujanga-70mm-jeedimetla",
            "venue_code": "BJNG",
            "city_slug": "hyderabad",
            "address": "Pipe Line Road, Phase 1, Shapur Nagar, Jeedimetla, Near Ranga Theatre, Hyderabad, Telangana 500055, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/bhujanga-70mm-jeedimetla/buytickets/BJNG"
        },
        {
            "name": "Aradhana Theatre: Hyderabad",
            "slug": "aradhana-theatre-hyderabad",
            "venue_code": "ARTH",
            "city_slug": "hyderabad",
            "address": "Professors Quarters, Inner Ring Road, Opposite Big Bazaar, Hyderabad, Telangana 500017, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/aradhana-theatre-hyderabad/buytickets/ARTH"
        },
        {
            "name": "Sri Krishna 70MM: Uppal",
            "slug": "sri-krishna-70mm-uppal",
            "venue_code": "SRKR",
            "city_slug": "hyderabad",
            "address": "Uppal Main Road, Opposite Uppal Bus Stand, Hanumasai Nagar, Vijayapuri Colony, Uppal, Hyderabad, Telangana 500039, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sri-krishna-70mm-uppal/buytickets/SRKR"
        },
        {
            "name": "Ramakrishna 35mm: Abids",
            "slug": "ramakrishna-35mm-abids",
            "venue_code": "RMKN",
            "city_slug": "hyderabad",
            "address": "NTR Estate, JN Road, Hyderabad, Telangana 500001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/ramakrishna-35mm-abids/buytickets/RMKN"
        },
        {
            "name": "Sree Sai Raja Theatre: Musheerabad",
            "slug": "sree-sai-raja-theatre-musheerabad",
            "venue_code": "SSRJ",
            "city_slug": "hyderabad",
            "address": "Dayara, Musheerabad, Zamistanpur, Kavadiguda, Musheerabad Main Road, Opposite Care Hospital, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sree-sai-raja-theatre-musheerabad/buytickets/SSRJ"
        },
        {
            "name": "Kumar Theatre: Kachiguda",
            "slug": "kumar-theatre-kachiguda",
            "venue_code": "KTKT",
            "city_slug": "hyderabad",
            "address": "3-2-1/1, Kachiguda Main Road, Mahalaxmi Nilayam, Kachiguda, Hyderabad, Telangana 500027, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/kumar-theatre-kachiguda/buytickets/KTKT"
        },
        {
            "name": "Santosh Theatre: Ibrahimpatnam",
            "slug": "santosh-theatre-ibrahimpatnam",
            "venue_code": "SNIB",
            "city_slug": "hyderabad",
            "address": "MRO Office Road, Ibrahimpatnam, Hyderabad, Telangana 501506, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/santosh-theatre-ibrahimpatnam/buytickets/SNIB"
        },
        {
            "name": "Laxmi 70MM A/C LASER DOLBY 7.1: Shamshabad",
            "slug": "laxmi-70mm-a-c-laser-dolby-7-1-shamshabad",
            "venue_code": "SLRT",
            "city_slug": "hyderabad",
            "address": "Laxmi Theatre Road, Rudra Colony, Hyderabad, Telangana 501218, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/laxmi-70mm-a-c-laser-dolby-7-1-shamshabad/buytickets/SLRT"
        },
        {
            "name": "Lakshmi Kala Mandir: Alwal",
            "slug": "lakshmi-kala-mandir-alwal",
            "venue_code": "LKMT",
            "city_slug": "hyderabad",
            "address": "Shop No: 14 - 69, Lothukunta Road, Lothkunta, Alwal, Secunderabad, Near Alwal City Bus Stop, Next to Sona Wines, Hyderabad, Telangana 500015, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/lakshmi-kala-mandir-alwal/buytickets/LKMT"
        },
        {
            "name": "Metro Cinema: Bahadurpura",
            "slug": "metro-cinema-bahadurpura",
            "venue_code": "MCBH",
            "city_slug": "hyderabad",
            "address": "Bahadurpura, Near Zoo Park Road, Hyderabad, Telangana 500064, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/metro-cinema-bahadurpura/buytickets/MCBH"
        },
        {
            "name": "Saptagiri 70MM 4K & Dolby Digital: RTC X Roads",
            "slug": "saptagiri-70mm-4k-dolby-digital-rtc-x-roads",
            "venue_code": "SART",
            "city_slug": "hyderabad",
            "address": "RTC X Road, Chikkadpally, Near Aakash Boys Hostel, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/saptagiri-70mm-4k-dolby-digital-rtc-x-roads/buytickets/SART"
        },
        {
            "name": "Sri Krishna Theatre: Aliabad (Shameerpet)",
            "slug": "sri-krishna-theatre-aliabad-shameerpet",
            "venue_code": "SKTA",
            "city_slug": "hyderabad",
            "address": "Near Ambedkar Statue, Aliabad, Shamirpet, Hyderabad, Telangana 500078, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sri-krishna-theatre-aliabad-shameerpet/buytickets/SKTA"
        },
        {
            "name": "Yakut Mahal Theater: Yakutpura",
            "slug": "yakut-mahal-theater-yakutpura",
            "venue_code": "YAKT",
            "city_slug": "hyderabad",
            "address": "17-3-224, AL Saboor Colony, Hyderabad, Telangana 500023, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/yakut-mahal-theater-yakutpura/buytickets/YAKT"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "Mahalaxmi Complex: Kothapet",
            "slug": "mahalaxmi-complex-kothapet",
            "venue_code": "MCKT",
            "city_slug": "hyderabad",
            "address": "Laxmi Nagar Colony, Kothapet Road, Near Axis Bank, Hyderabad, Telangana 500102, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/mahalaxmi-complex-kothapet/buytickets/MCKT"
        },
        # Multiplexes
        {
            "name": "AMB Cinemas: Gachibowli",
            "slug": "amb-cinemas-gachibowli",
            "venue_code": "AMBH",
            "city_slug": "hyderabad",
            "address": "Sarath City Capital Mall, Forest Dept Colony, Kondapur, Gachibowli - Miyapur Road, White Field Road, Opposite Mahindra Showroom, Hyderabad, Telangana 500084, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/amb-cinemas-gachibowli/buytickets/AMBH"
        },
        {
            "name": "Prasads Multiplex: Hyderabad",
            "slug": "prasads-multiplex-hyderabad",
            "venue_code": "PRHN",
            "city_slug": "hyderabad",
            "address": "Khairtabad, IMAX Road, NTR Marg, Near NTR Gardens, Hyderabad, Telangana 500063, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/prasads-multiplex-hyderabad/buytickets/PRHN"
        },
        {
            "name": "Asian Lakshmikala Cinepride: Moosapet",
            "slug": "asian-lakshmikala-cinepride-moosapet",
            "venue_code": "ACPM",
            "city_slug": "hyderabad",
            "address": "Street Number 4, SP Nagar, Bharat Nagar,Moosapet, Opposite Sri Ramulu Theatre, Hyderabad, Telangana 500018, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-lakshmikala-cinepride-moosapet/buytickets/ACPM"
        },
        {
            "name": "ALLU Cinemas: Kokapet",
            "slug": "allu-cinemas-kokapet",
            "venue_code": "ALUC",
            "city_slug": "hyderabad",
            "address": "Plot 20, Adjacent to Allu Studios, Power Welfare Society, Narsingi, Hyderabad, Telangana 500075, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/allu-cinemas-kokapet/buytickets/ALUC"
        },
        {
            "name": "ART CINEMAS: Vanasthalipuram",
            "slug": "art-cinemas-vanasthalipuram",
            "venue_code": "ACEV",
            "city_slug": "hyderabad",
            "address": "Door. No.5-5-185 and 5-5-186,Sy.No.53 and 56, 4th Floor, TATTVA MALL, Vanasthalipuram, Saheb Nagar Khurd, Hyderabad, Telangana 500070, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/art-cinemas-vanasthalipuram/buytickets/ACEV"
        },
        {
            "name": "Aparna Cinemas: Nallagandla",
            "slug": "aparna-cinemas-nallagandla",
            "venue_code": "AACN",
            "city_slug": "hyderabad",
            "address": "Nallagandla Road, HUDA Layout, Hyderabad, Telangana 500019, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/aparna-cinemas-nallagandla/buytickets/AACN"
        },
        {
            "name": "PVR: Nexus Mall Kukatpally, Hyderabad",
            "slug": "pvr-nexus-mall-kukatpally-hyderabad",
            "venue_code": "PVFS",
            "city_slug": "hyderabad",
            "address": "4th Floor, Nexus Mall, Plot No S-16, Survey No.1009, KPHB Phase 6, Opp Malaysian Township, Kukatpally, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-nexus-mall-kukatpally-hyderabad/buytickets/PVFS"
        },
        {
            "name": "AAA Cinemas: Ameerpet",
            "slug": "aaa-cinemas-ameerpet",
            "venue_code": "ACAS",
            "city_slug": "hyderabad",
            "address": "Asian Allu Arjun Cinemas, Satyam Theatre Road, X Road Kumar Basti, Ameerpet, Hyderabad, Telangana 500082, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/aaa-cinemas-ameerpet/buytickets/ACAS"
        },
        {
            "name": "Cinepolis: TNR North City, Suchitra, Hyderabad",
            "slug": "cinepolis-tnr-north-city-suchitra-hyderabad",
            "venue_code": "CTNR",
            "city_slug": "hyderabad",
            "address": "Cinepolis TNR North City, SY No 85 and 89, NH-44, 7, Suchitra Road, NH-44, 7, Suchitra Road, Hyderabad, Telangana 500055, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cinepolis-tnr-north-city-suchitra-hyderabad/buytickets/CTNR"
        },
        {
            "name": "Miraj Cinemas: CineTown, Miyapur",
            "slug": "miraj-cinemas-cinetown-miyapur",
            "venue_code": "MMCA",
            "city_slug": "hyderabad",
            "address": "Cinetown, Survey No. 71, Miyapur Village Ranga Reddy, Hyderabad, Telangana 500049, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/miraj-cinemas-cinetown-miyapur/buytickets/MMCA"
        },
        {
            "name": "INOX: GSM Mall, Hyderabad",
            "slug": "inox-gsm-mall-hyderabad",
            "venue_code": "IGMH",
            "city_slug": "hyderabad",
            "address": "INOX Leisure Ltd, 4th floor, GSM Mall, Miyapur Main Road, Madinaguda, Hyderabad, Telangana 500049, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-gsm-mall-hyderabad/buytickets/IGMH"
        },
        {
            "name": "PVR Lakeshore PXL 4K Laser ATMOS DTS-X Y Junction",
            "slug": "pvr-lakeshore-pxl-4k-laser-atmos-dts-x-y-junction",
            "venue_code": "ILKS",
            "city_slug": "hyderabad",
            "address": "3rd Floor, Lake Shore Mall, IDA Kukatpally, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-lakeshore-pxl-4k-laser-atmos-dts-x-y-junction/buytickets/ILKS"
        },
        {
            "name": "Cineverse Multiplex: Uppal",
            "slug": "cineverse-multiplex-uppal",
            "venue_code": "CVMU",
            "city_slug": "hyderabad",
            "address": "Main Road, IBP Petrol Bunk, Shanthi Nagar, Medchal Malkajgiri, Hyderabad, Telangana 500039, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cineverse-multiplex-uppal/buytickets/CVMU"
        },
        {
            "name": "Cinepolis: Lulu Mall, Hyderabad",
            "slug": "cinepolis-lulu-mall-hyderabad",
            "venue_code": "CPMH",
            "city_slug": "hyderabad",
            "address": "3rd Floor, Survey No.1050, KPBH Colony Phase-3, LuLu Mall,Opposite - JNTU Hi-Tech Road, Kukatpally, Kukatpally, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cinepolis-lulu-mall-hyderabad/buytickets/CPMH"
        },
        {
            "name": "GPR Multiplex: Nizampet, Hyderabad",
            "slug": "gpr-multiplex-nizampet-hyderabad",
            "venue_code": "GPRH",
            "city_slug": "hyderabad",
            "address": "Nizampet X Roads, Kukatpally, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/gpr-multiplex-nizampet-hyderabad/buytickets/GPRH"
        },
        {
            "name": "Asian Cinemart: RC Puram",
            "slug": "asian-cinemart-rc-puram",
            "venue_code": "ASHN",
            "city_slug": "hyderabad",
            "address": "Sy. No. 101AA, 101 E, 105 E, Ramchandra Puram, Hyderabad, Telangana 500133, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-cinemart-rc-puram/buytickets/ASHN"
        },
        {
            "name": "Bhramaramba 70MM A/C 4K Dolby: Kukatpally",
            "slug": "bhramaramba-70mm-a-c-4k-dolby-kukatpally",
            "venue_code": "BRKH",
            "city_slug": "hyderabad",
            "address": "Jai Bharat Nagar, Hyder Nagar, Vasantha Nagar, Kukatpally, Near Karachi Bakery, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/bhramaramba-70mm-a-c-4k-dolby-kukatpally/buytickets/BRKH"
        },
        {
            "name": "Mallikarjuna 70mm A/C DTS: Kukatpally",
            "slug": "mallikarjuna-70mm-a-c-dts-kukatpally",
            "venue_code": "MAHM",
            "city_slug": "hyderabad",
            "address": "1-2-29/93, Jai Bharat Nagar, Hyder Nagar, Vasantha Nagar, Nizampet, Hyderabad, Telangana 500090, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/mallikarjuna-70mm-a-c-dts-kukatpally/buytickets/MAHM"
        },
        {
            "name": "Asian M Cube Mall: Attapur",
            "slug": "asian-m-cube-mall-attapur",
            "venue_code": "AMCA",
            "city_slug": "hyderabad",
            "address": "1st Floor, MCube Mall, Attapur Ring Road, Somi Reddy Nagar, Rajendra Nagar,Attapur, Hyderabad, Telangana 500048, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-m-cube-mall-attapur/buytickets/AMCA"
        },
        {
            "name": "Asian Cineplanet Multiplex: Kompally",
            "slug": "asian-cineplanet-multiplex-kompally",
            "venue_code": "CPHY",
            "city_slug": "hyderabad",
            "address": "Satyam Enclave, Medchal Road, Kompally, Hyderabad, Telangana 500014, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-cineplanet-multiplex-kompally/buytickets/CPHY"
        },
        {
            "name": "Cinepolis: DSL Virtue Mall Uppal, Hyderabad",
            "slug": "cinepolis-dsl-virtue-mall-uppal-hyderabad",
            "venue_code": "ABCS",
            "city_slug": "hyderabad",
            "address": "DSL Virtue Mall, 3rd Floor, Plot No. B-1, B-2B and 2, Uppal Khlasa VRR, Near Indian Oil Petrol Pump, Hyderabad, Telangana 500039, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cinepolis-dsl-virtue-mall-uppal-hyderabad/buytickets/ABCS"
        },
        {
            "name": "PVR: Next Galleria Mall, Panjagutta",
            "slug": "pvr-next-galleria-mall-panjagutta",
            "venue_code": "PNNG",
            "city_slug": "hyderabad",
            "address": "Next Galleria Mall, 4th Floor, PVR Limited, Panjagutta, Opposite Panjaguttta Metro Station, Hyderabad, Telangana 500082, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-next-galleria-mall-panjagutta/buytickets/PNNG"
        },
        {
            "name": "PVR: Atrium Gachibowli, Hyderabad",
            "slug": "pvr-atrium-gachibowli-hyderabad",
            "venue_code": "PVTS",
            "city_slug": "hyderabad",
            "address": "4th Floor, Atrium Mall, Survey No. 136, Gachibowli- Miyapur Road, Gachibowli, Hyderabad, Telangana 500032, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-atrium-gachibowli-hyderabad/buytickets/PVTS"
        },
        {
            "name": "INOX: Ashoka One, 4K LASER Dolby ATMOS: Kukatpally",
            "slug": "inox-ashoka-one-4k-laser-dolby-atmos-kukatpally",
            "venue_code": "AKYJ",
            "city_slug": "hyderabad",
            "address": "INOX Leisure Ltd,3rd Floor, Ashoka One Mall, Kukatpally Y-Junction, Hyderabad, Telangana 500072, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-ashoka-one-4k-laser-dolby-atmos-kukatpally/buytickets/AKYJ"
        },
        {
            "name": "INOX: Sattva Necklace Mall, Kavadiguda",
            "slug": "inox-sattva-necklace-mall-kavadiguda",
            "venue_code": "ISTN",
            "city_slug": "hyderabad",
            "address": "INOX Leisure Ltd, 4th Floor, Sattva Necklace Mall, Kavadiguda Main Road, Secunderabad, Hyderabad, Telangana 500080, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-sattva-necklace-mall-kavadiguda/buytickets/ISTN"
        },
        {
            "name": "JP Cinemas: Chandanagar",
            "slug": "jp-cinemas-chandanagar",
            "venue_code": "JJPP",
            "city_slug": "hyderabad",
            "address": "Shop No. W-4, Tapadia Maruti Infinity Mall, Door No. 2-132, Chanda Nagar, Hyderabad, Telangana 500050, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/jp-cinemas-chandanagar/buytickets/JJPP"
        },
        {
            "name": "Cinepolis: Mantra Mall, Attapur",
            "slug": "cinepolis-mantra-mall-attapur",
            "venue_code": "CMMA",
            "city_slug": "hyderabad",
            "address": "Mantra Mall, Inner Ring Road, Royal Colony, Upparpally, Hyderabad, Telangana 500030, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cinepolis-mantra-mall-attapur/buytickets/CMMA"
        },
        {
            "name": "PVR: Preston, Gachibowli Hyderabad",
            "slug": "pvr-preston-gachibowli-hyderabad",
            "venue_code": "PVTP",
            "city_slug": "hyderabad",
            "address": "Preston Mall, No: 62, Hitech City Main Road, Lumbini Avenue, Gachibowli, Hyderabad, Telangana 500081, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-preston-gachibowli-hyderabad/buytickets/PVTP"
        },
        {
            "name": "Asian Radhika Multiplex: ECIL",
            "slug": "asian-radhika-multiplex-ecil",
            "venue_code": "ARMH",
            "city_slug": "hyderabad",
            "address": "Anupuram Colony, Dr A S Rao Nagar Road, ECIL Main Road, Near Parivaar Banquet Halls, Hyderabad, Telangana 500062, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-radhika-multiplex-ecil/buytickets/ARMH"
        },
        {
            "name": "Aparna Cinemas: Shamshabad",
            "slug": "aparna-cinemas-shamshabad",
            "venue_code": "APNS",
            "city_slug": "hyderabad",
            "address": "1/97/11, Sathamrai Village, Langerguda, Hyderabad, Telangana 500052, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/aparna-cinemas-shamshabad/buytickets/APNS"
        },
        {
            "name": "Asian Sha & Shahensha: Chintal",
            "slug": "asian-sha-shahensha-chintal",
            "venue_code": "ACHI",
            "city_slug": "hyderabad",
            "address": "Jeedimetla Main Road, Ganesh Nagar, Jeedimetla, Dee Nagar, Balanagar, Hyderabad, Telangana 500037, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-sha-shahensha-chintal/buytickets/ACHI"
        },
        {
            "name": "INOX: Odeon 4K, LASER, ATMOS, DTS-X: RTC X Roads",
            "slug": "inox-odeon-4k-laser-atmos-dts-x-rtc-x-roads",
            "venue_code": "IOMH",
            "city_slug": "hyderabad",
            "address": "Odeon Mall, Chikkadpally, New Nallakunta, Hyderabad, Telangana 500020, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-odeon-4k-laser-atmos-dts-x-rtc-x-roads/buytickets/IOMH"
        },
        {
            "name": "PVR: Irrum Manzil, Hyderabad",
            "slug": "pvr-irrum-manzil-hyderabad",
            "venue_code": "PIMH",
            "city_slug": "hyderabad",
            "address": "Level 5, Shop No.01, Hyderabad Next Galleria@Irrum Manzil, Survey No. TS.No.3/1, Ward No. 85,  Block-E, Khairatabad, Hyderabad, Telangana 500082, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-irrum-manzil-hyderabad/buytickets/PIMH"
        },
        {
            "name": "PVR ICON: Hitech, Madhapur, Hyderabad",
            "slug": "pvr-icon-hitech-madhapur-hyderabad",
            "venue_code": "PVHM",
            "city_slug": "hyderabad",
            "address": "4th Floor, Next Galleria Mall, Sy. No. 64, Hitech City, Madhapur, Jaihind Enclave, Serilingampally, Hyderabad, Telangana 500081, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-icon-hitech-madhapur-hyderabad/buytickets/PVHM"
        },
        {
            "name": "Asian Mukta A2 Sensation Cinema: Kairathabad",
            "slug": "asian-mukta-a2-sensation-cinema-kairathabad",
            "venue_code": "SNKH",
            "city_slug": "hyderabad",
            "address": "Lakdikapul Road, Vasavi Nagar, Khairtabad, Hyderabad, Telangana 500004, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-mukta-a2-sensation-cinema-kairathabad/buytickets/SNKH"
        },
        {
            "name": "INOX: Prism Mall, Hyderabad",
            "slug": "inox-prism-mall-hyderabad",
            "venue_code": "IPRS",
            "city_slug": "hyderabad",
            "address": "PVR INOX Limited, 3rd Floor, Prism Mall, Near Gachibowli Cross Roads, Hyderabad, Telangana 500032, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-prism-mall-hyderabad/buytickets/IPRS"
        },
        {
            "name": "PVR: Musarambagh, Hyderabad",
            "slug": "pvr-musarambagh-hyderabad",
            "venue_code": "PVUM",
            "city_slug": "hyderabad",
            "address": "Ts No 2,5 and 6, Ward No. 170, Level 5, 11, NH65, Andhra Colony, New Malakpet, Hyderabad, Telangana 500036, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-musarambagh-hyderabad/buytickets/PVUM"
        },
        {
            "name": "Miraj Cinemas: Anand Mall and Movies, Narsingi",
            "slug": "miraj-cinemas-anand-mall-and-movies-narsingi",
            "venue_code": "MRAD",
            "city_slug": "hyderabad",
            "address": "Anand Mall and Movies, Narsingi Village, Hyderabad, Telangana 500075, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/miraj-cinemas-anand-mall-and-movies-narsingi/buytickets/MRAD"
        },
        {
            "name": "PVR Superplex Inorbit: LUXE, PXL, 4DX: Cyberabad",
            "slug": "pvr-superplex-inorbit-luxe-pxl-4dx-cyberabad",
            "venue_code": "PIIC",
            "city_slug": "hyderabad",
            "address": "5th Floor, APIIC Software Layout, Mindspace, Inorbit Mall, Hitech City, Madhapur, Cyberabad, Hyderabad, Telangana 500081, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-superplex-inorbit-luxe-pxl-4dx-cyberabad/buytickets/PIIC"
        },
        {
            "name": "Miraj Cinemas: Shalini Shivani, Kothapet",
            "slug": "miraj-cinemas-shalini-shivani-kothapet",
            "venue_code": "MCSS",
            "city_slug": "hyderabad",
            "address": "Opposite Kothapet Fruit Market, Beside Reddy Bar and Restaurant, Kothapet Near Induss Hospital, Hyderabad, Telangana 500036, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/miraj-cinemas-shalini-shivani-kothapet/buytickets/MCSS"
        },
        {
            "name": "Asian Jyothi: RC Puram",
            "slug": "asian-jyothi-rc-puram",
            "venue_code": "ASJY",
            "city_slug": "hyderabad",
            "address": "Jyothi Nagar, Ashok Nagar, Chanda Nagar, Opposite TVS Motors, Near Brilliant Junior College, Hyderabad, Telangana 502032, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-jyothi-rc-puram/buytickets/ASJY"
        },
        {
            "name": "Asian Super Cinema: Balapur",
            "slug": "asian-super-cinema-balapur",
            "venue_code": "SPCB",
            "city_slug": "hyderabad",
            "address": "Balapur, Cross Road, Near Canara Bank ATM, Hyderabad, Telangana 500005, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-super-cinema-balapur/buytickets/SPCB"
        },
        {
            "name": "Miraj Cinemas: A2A Central Mall, Balanagar",
            "slug": "miraj-cinemas-a2a-central-mall-balanagar",
            "venue_code": "MRAA",
            "city_slug": "hyderabad",
            "address": "A2A Central Mall, 4th Floor, Adarsh Nagar, Hyderabad, Telangana 500037, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/miraj-cinemas-a2a-central-mall-balanagar/buytickets/MRAA"
        },
        {
            "name": "PVR: Central Mall, Panjagutta",
            "slug": "pvr-central-mall-panjagutta",
            "venue_code": "PVYH",
            "city_slug": "hyderabad",
            "address": "5th Floor, Hyderabad Central Mall, Punjagutta Cross Road, Opposite Traffic Police Station Panjagutta, Hyderabad, Telangana 500082, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-central-mall-panjagutta/buytickets/PVYH"
        },
        {
            "name": "Asian Rajya Lakshmi: Uppal",
            "slug": "asian-rajya-lakshmi-uppal",
            "venue_code": "ARYH",
            "city_slug": "hyderabad",
            "address": "Raj Laxmi Theater, 2-1-40, Uppal Ring Road, Raj Nagar, Uppal, Near Indane Gas Service, Hyderabad, Telangana 500039, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-rajya-lakshmi-uppal/buytickets/ARYH"
        },
        {
            "name": "Miraj Cinemas: Raghavendra, Malkajgiri",
            "slug": "miraj-cinemas-raghavendra-malkajgiri",
            "venue_code": "MRRG",
            "city_slug": "hyderabad",
            "address": "Bus Stand, Raghavendra Theatre Road, Malkajgiri, Hyderabad, Telangana 500047, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/miraj-cinemas-raghavendra-malkajgiri/buytickets/MRRG"
        },
        {
            "name": "Tivoli Cinemas: Secunderabad",
            "slug": "tivoli-cinemas-secunderabad",
            "venue_code": "TVHY",
            "city_slug": "hyderabad",
            "address": "Gunrock Enclave, NCC Ground, General Choudhuri Road, Secunderabad, Hyderabad, Telangana 500003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/tivoli-cinemas-secunderabad/buytickets/TVHY"
        },
        {
            "name": "INOX: Maheshwari Parmeshwari Mall, Kachiguda",
            "slug": "inox-maheshwari-parmeshwari-mall-kachiguda",
            "venue_code": "INMH",
            "city_slug": "hyderabad",
            "address": "5th Floor, Maheshwari Parmeshwari Mall, Kachiguda Cross Roads, Hyderabad, Telangana 500027, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-maheshwari-parmeshwari-mall-kachiguda/buytickets/INMH"
        },
        {
            "name": "INOX: SMR Vinay Metro Mall, Dolby ATMOS: Miyapur",
            "slug": "inox-smr-vinay-metro-mall-dolby-atmos-miyapur",
            "venue_code": "IVNM",
            "city_slug": "hyderabad",
            "address": "6th floor, SMR Vinay Metro Mall, Miyapur, Hyderabad, Telangana 500049, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-smr-vinay-metro-mall-dolby-atmos-miyapur/buytickets/IVNM"
        },
        {
            "name": "INOX GVK One, Banjara Hills: Hyderabad",
            "slug": "inox-gvk-one-banjara-hills-hyderabad",
            "venue_code": "INHY",
            "city_slug": "hyderabad",
            "address": "4th Floor, GVK One Mall, Road No.1, Banjara Hills, Opposite Hyatt Place, Hyderabad, Telangana 500034, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/inox-gvk-one-banjara-hills-hyderabad/buytickets/INHY"
        },
        {
            "name": "Miraj Cinemas: Geeta, Chandanagar",
            "slug": "miraj-cinemas-geeta-chandanagar",
            "venue_code": "MRGT",
            "city_slug": "hyderabad",
            "address": "H.No 5 - 54, Manjeera Road, Chandanagar, Beside Andhra Bank, Hyderabad, Telangana 500050, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/miraj-cinemas-geeta-chandanagar/buytickets/MRGT"
        },
        {
            "name": "PVR: RK Cineplex, Hyderabad",
            "slug": "pvr-rk-cineplex-hyderabad",
            "venue_code": "PRCX",
            "city_slug": "hyderabad",
            "address": "Plot No.1, RK Complex, Road No.2, Oppsite L V Prasad Eye Hospital, Venkat Nagar, Banjara Hills, BNR Colony, Hyderabad, Telangana 500034, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/pvr-rk-cineplex-hyderabad/buytickets/PRCX"
        },
        {
            "name": "Asian Mukund Cinema: Medchal",
            "slug": "asian-mukund-cinema-medchal",
            "venue_code": "AMCM",
            "city_slug": "hyderabad",
            "address": "Medchal Road, National Highway 44, Near City Union Bank, Secunderabad, Opposite RK Lodge, Hyderabad, Telangana 501401, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-mukund-cinema-medchal/buytickets/AMCM"
        },
        {
            "name": "Cinepolis: CCPL Mall Malkajgiri, Hyderabad",
            "slug": "cinepolis-ccpl-mall-malkajgiri-hyderabad",
            "venue_code": "CPCL",
            "city_slug": "hyderabad",
            "address": "CCPL Mall, Malkajgiri Road, Vimala Devi Nagar Colony, Malkajgiri, Hyderabad, Telangana 500047, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cinepolis-ccpl-mall-malkajgiri-hyderabad/buytickets/CPCL"
        },
        {
            "name": "Movietime Cinemas: SKY Mall, Erragadda X Road",
            "slug": "movietime-cinemas-sky-mall-erragadda-x-road",
            "venue_code": "PSMJ",
            "city_slug": "hyderabad",
            "address": "SKY Mall, 3rd Floor, Erragadda X  Road, Czech Colony, Hyderabad, Telangana 500018, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/movietime-cinemas-sky-mall-erragadda-x-road/buytickets/PSMJ"
        },
        {
            "name": "Cinepolis: Sudha Cinemas, Hyderabad",
            "slug": "cinepolis-sudha-cinemas-hyderabad",
            "venue_code": "STHD",
            "city_slug": "hyderabad",
            "address": "Shah Ali Banda New Road, Rajpal Nagar, Sudha Theatre Road, Hyderabad, Telangana 500065, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/cinepolis-sudha-cinemas-hyderabad/buytickets/STHD"
        },
        {
            "name": "Asian Tarakarama Cineplex: Kachiguda",
            "slug": "asian-tarakarama-cineplex-kachiguda",
            "venue_code": "TRHY",
            "city_slug": "hyderabad",
            "address": "Kachiguda X Road, Beside Big Bazar, Rajamohallah, King Koti, Kachiguda, Beside Big Bazar, Opposite Dhana Lakshmi Bank, Hyderabad, Telangana 500027, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/asian-tarakarama-cineplex-kachiguda/buytickets/TRHY"
        },
        {
            "name": "CONNPLEX Luxuriance Cinemas: Mpm Mall, Banjara Hil",
            "slug": "connplex-luxuriance-cinemas-mpm-mall-banjara-hil",
            "venue_code": "CPLK",
            "city_slug": "hyderabad",
            "address": "4th Floor, MPM Timesquare Mall, Nagarjuna Circle, Road No.1 and 3, Banjara Hills, Hyderabad, Telangana 500034, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/connplex-luxuriance-cinemas-mpm-mall-banjara-hil/buytickets/CPLK"
        },
        {
            "name": "Sree Ramana 70MM 4K Laser & Dolby 7.1: Amberpet",
            "slug": "sree-ramana-70mm-4k-laser-dolby-7-1-amberpet",
            "venue_code": "SRCA",
            "city_slug": "hyderabad",
            "address": "2-2-1053, Bagh Amberpet, Near Durga Matha Temple, Hyderabad, Telangana 500013, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sree-ramana-70mm-4k-laser-dolby-7-1-amberpet/buytickets/SRCA"
        },
        {
            "name": "Sree Ramana Gold 4K & Dolby 7.1: Amberpet",
            "slug": "sree-ramana-gold-4k-dolby-7-1-amberpet",
            "venue_code": "SRCH",
            "city_slug": "hyderabad",
            "address": "2-2-1053, Bagh Amberpet, Near Durga Matha Temple, Hyderabad, Telangana 500013, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/sree-ramana-gold-4k-dolby-7-1-amberpet/buytickets/SRCH"
        },
        {
            "name": "ROONGTA CINEMAS: NOVUM, NAMPALLY",
            "slug": "roongta-cinemas-novum-nampally",
            "venue_code": "RCNH",
            "city_slug": "hyderabad",
            "address": "Latha Talkies, Sri Balaji Enclave, Ghosha Mahal, Nampally, Hyderabad, Telangana 500001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/hyderabad/roongta-cinemas-novum-nampally/buytickets/RCNH"
        }
    ],

    # --------------------------------------------------------------------------
    # 9. WARANGAL
    # --------------------------------------------------------------------------
    "warangal": [
        # Single Screens
        {
            "name": "Amrutha Cinema: Hanumakonda",
            "slug": "amrutha-cinema-hanumakonda",
            "venue_code": "ACWH",
            "city_slug": "warangal",
            "address": "Warangal - Hyderabad Road, Enugula Gadda, Hanmakonda, Near Amrutha Gardens Marriage Hall, Warangal, Telangana 506001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/amrutha-cinema-hanumakonda/buytickets/ACWH"
        },
        {
            "name": "Venkatrama 70MM 2k Barco Laser: Warangal",
            "slug": "venkatrama-70mm-2k-barco-laser-warangal",
            "venue_code": "VKTR",
            "city_slug": "warangal",
            "address": "Narsampet Road, Kashibugga, Warangal, Telangana 506002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/venkatrama-70mm-2k-barco-laser-warangal/buytickets/VKTR"
        },
        {
            "name": "Radhika Theatre: Warangal",
            "slug": "radhika-theatre-warangal",
            "venue_code": "RTWA",
            "city_slug": "warangal",
            "address": "Radhika Theater Lane, Near Indian Overseas Bank ATM, Behind Petrol Pump, Warangal, Telangana 506002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/radhika-theatre-warangal/buytickets/RTWA"
        },
        {
            "name": "Bhavani Picture Palace: Kazipet",
            "slug": "bhavani-picture-palace-kazipet",
            "venue_code": "JTBP",
            "city_slug": "warangal",
            "address": "Hyderabad-Warangal-Bhopalpatnam Road, Rahamatnagar, Main Road, Warangal, Telangana 506003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/bhavani-picture-palace-kazipet/buytickets/JTBP"
        },
        # Mixed / Twin / Complex Screens
        {
            "name": "Asian Gemini Theatre: Warangal",
            "slug": "asian-gemini-theatre-warangal",
            "venue_code": "ASGM",
            "city_slug": "warangal",
            "address": "SVN Road, Mattewada, Phatak Mohalla, Warangal, Telangana 506002, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/asian-gemini-theatre-warangal/buytickets/ASGM"
        },
        # Multiplexes
        {
            "name": "Asian Sridevi Multiplex: Hanumakonda",
            "slug": "asian-sridevi-multiplex-hanumakonda",
            "venue_code": "ASMW",
            "city_slug": "warangal",
            "address": "Asian Sridevi Mall, Bus Stand Road, Sai Nagar, Hanmakonda, Warangal, Telangana 506001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/asian-sridevi-multiplex-hanumakonda/buytickets/ASMW"
        },
        {
            "name": "PVR: Warangal, Maddox Mall",
            "slug": "pvr-warangal-maddox-mall",
            "venue_code": "PWLM",
            "city_slug": "warangal",
            "address": "Near Post Office, Girmajipet, Warangal, Telangana 506001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/pvr-warangal-maddox-mall/buytickets/PWLM"
        },
        {
            "name": "Asian Ashoka Air-Conditioned: Hanumakonda",
            "slug": "asian-ashoka-air-conditioned-hanumakonda",
            "venue_code": "AAPW",
            "city_slug": "warangal",
            "address": "Ashoka A plex, Beside Warangal Hyderabad Highway, Near Govt Juniour College, Warangal, Telangana 506001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/asian-ashoka-air-conditioned-hanumakonda/buytickets/AAPW"
        },
        {
            "name": "Sambhavi Theatre: Kazipet",
            "slug": "sambhavi-theatre-kazipet",
            "venue_code": "SMBH",
            "city_slug": "warangal",
            "address": "Hyderabad-Warangal-Bhopalpatnam Road, Rahamatnagar, Main Road, Warangal, Telangana 506003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/warangal/sambhavi-theatre-kazipet/buytickets/SMBH"
        }
    ],

    # --------------------------------------------------------------------------
    # 10. KARIMNAGAR
    # --------------------------------------------------------------------------
    "karimnagar": [
        # Multiplexes
        {
            "name": "Asian Paradise Cinemas: Karimnagar",
            "slug": "asian-paradise-cinemas-karimnagar",
            "venue_code": "APCY",
            "city_slug": "karimnagar",
            "address": "C4RJ+9WW, Sharma Nagar, Karimnagar, Telangana 505001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/karimnagar/asian-paradise-cinemas-karimnagar/buytickets/APCY"
        },
        {
            "name": "1 Cinemas by Asian Mukta A2 Cinemas, SN Pride Mall",
            "slug": "1-cinemas-by-asian-mukta-a2-cinemas-sn-pride-mall",
            "venue_code": "AMSN",
            "city_slug": "karimnagar",
            "address": "SN Pride Mall, 2nd Floor, Gandhi Road, Kisan Nagar, Karimnagar, Telangana 505451, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/karimnagar/1-cinemas-by-asian-mukta-a2-cinemas-sn-pride-mall/buytickets/AMSN"
        },
        {
            "name": "Asian Mukta A2 Srinivasa Theatre: Karimnagar",
            "slug": "asian-mukta-a2-srinivasa-theatre-karimnagar",
            "venue_code": "AMST",
            "city_slug": "karimnagar",
            "address": "Srinivasa Theatre Road, Shasha Mahala, Ashoknagar, Near Kakatiya Techno School, Karimnagar, Telangana 505001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/karimnagar/asian-mukta-a2-srinivasa-theatre-karimnagar/buytickets/AMST"
        }
    ],

    # --------------------------------------------------------------------------
    # 11. NIZAMABAD
    # --------------------------------------------------------------------------
    "nizamabad": [
        # Multiplexes
        {
            "name": "PVR: Venu Mall, Nizamabad",
            "slug": "pvr-venu-mall-nizamabad",
            "venue_code": "PRVN",
            "city_slug": "nizamabad",
            "address": "3th Floor, VENU MALL H. NO. 5-6-661, Pragathi Nagar, Nizamabad, Telangana 503003, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/nizamabad/pvr-venu-mall-nizamabad/buytickets/PRVN"
        },
        {
            "name": "Asian Usha Prasad Multiplex: Nizamabad",
            "slug": "asian-usha-prasad-multiplex-nizamabad",
            "venue_code": "AUPM",
            "city_slug": "nizamabad",
            "address": "Kotagally, Pedda Bazaar Road, Shivaji Nagar, Near Government High School, Nizamabad, Telangana 503001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/nizamabad/asian-usha-prasad-multiplex-nizamabad/buytickets/AUPM"
        }
    ],

    # --------------------------------------------------------------------------
    # 12. KHAMMAM
    # --------------------------------------------------------------------------
    "khammam": [
        # Single Screens
        {
            "name": "Vinoda 4K Dolby Atmos: Khammam",
            "slug": "vinoda-4k-dolby-atmos-khammam",
            "venue_code": "VCKM",
            "city_slug": "khammam",
            "address": "Mayuri Center, Braman Bazar, Mamillagudem, Near Bus Stand, Khammam, Telangana 507001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/khammam/vinoda-4k-dolby-atmos-khammam/buytickets/VCKM"
        },
        # Multiplexes
        {
            "name": "Asian Srinivasa: Khammam",
            "slug": "asian-srinivasa-khammam",
            "venue_code": "ASSK",
            "city_slug": "khammam",
            "address": "9-2-15/A, Station Road, Braman Bazar, Khammam, Telangana 507001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/khammam/asian-srinivasa-khammam/buytickets/ASSK"
        }
    ],

    # --------------------------------------------------------------------------
    # 13. MAHABUBNAGAR
    # --------------------------------------------------------------------------
    "mahabubnagar": [
        # Single Screens
        {
            "name": "Venkateswara Theatre: Mahbubnagar",
            "slug": "venkateswara-theatre-mahbubnagar",
            "venue_code": "VTMB",
            "city_slug": "mahbubnagar",
            "address": "Shah Saheb Gutta, Near Srinivasa Theatre, Mahbubnagar, Telangana 509001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/mahbubnagar/venkateswara-theatre-mahbubnagar/buytickets/VTMB"
        },
        # Multiplexes
        {
            "name": "AVD Cinemas: Mahbubnagar",
            "slug": "avd-cinemas-mahbubnagar",
            "venue_code": "AVDM",
            "city_slug": "mahbubnagar",
            "address": "Shah Saheb Gutta, Boyapalle Rural, Near Sri Hanuman Temple, Mahbubnagar, Telangana 509001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/mahbubnagar/avd-cinemas-mahbubnagar/buytickets/AVDM"
        },
        {
            "name": "Asian Srinivasa: Mahbubnagar",
            "slug": "asian-srinivasa-mahbubnagar",
            "venue_code": "ASMH",
            "city_slug": "mahbubnagar",
            "address": "Shah Saheb Gutta, Opposite Rehmania Masjid, Near Model Basic High School, Mahbubnagar, Telangana 509001, India",
            "bms_url": "https://in.bookmyshow.com/cinemas/mahbubnagar/asian-srinivasa-mahbubnagar/buytickets/ASMH"
        }
    ]
}

# Alias city keys
BMS_THEATER_CATALOG["visakhapatnam"] = BMS_THEATER_CATALOG["vizag"]


# ==============================================================================
# DISTRICT (BY ZOMATO) THEATER CATALOG
# ==============================================================================
DISTRICT_THEATER_CATALOG = {
    # --------------------------------------------------------------------------
    # 1. VISAKHAPATNAM (VIZAG)
    # --------------------------------------------------------------------------
    "vizag": [
        {
            "name": "Melody 4K Dolby Atmos, Jagadamba Center, Vizag",
            "slug": "melody-4k-dolby-atmos-jagadamba-center-vizag-CD2432",
            "venue_code": "DST_MELV",
            "address": "Chitralaya Rd, beside V Max Theatre, Suryabagh, Jagadamba, Visakhapatnam",
            "url": "https://www.district.in/movies/melody-4k-dolby-atmos-jagadamba-center-vizag-CD2432"
        },
        {
            "name": "Sarat Theatre: A/C 4K Laser Dolby Atmos, Vizag",
            "slug": "sarat-theatre-a-c-4k-laser-dolby-atmos-vizag",
            "venue_code": "STTR",
            "bms_exclusive": True,
            "address": "Railway Station Road, Dondaparthy, Dwaraka Nagar, Vizag 530016",
            "url": "https://in.bookmyshow.com/cinemas/vizag-visakhapatnam/sarat-theatre-a-c-4k-laser-dolby-atmos-vizag/buytickets/STTR"
        },
        {
            "name": "Sangam Theatre, Dondaparthy, Vizag",
            "slug": "sangam-theatre-dondaparthy-vizag-CD677",
            "venue_code": "DST_SNGV",
            "address": "Railway Station Road, Dondaparthy, Dwaraka Nagar, Visakhapatnam",
            "url": "https://www.district.in/movies/sangam-theatre-dondaparthy-vizag-CD677"
        },
        {
            "name": "INOX: Varun Beach, Beach Road, Vizag",
            "slug": "inox-varun-beach-maharanipet-vizag-CD1029271",
            "venue_code": "DST_VBMV",
            "address": "Survey No.120 & 121, Varun Beach, Beach Road, Maharanipet, Visakhapatnam",
            "url": "https://www.district.in/movies/inox-varun-beach-maharanipet-vizag-CD1029271"
        },
        {
            "name": "INOX: CMR Central, Maddilapalem, Vizag",
            "slug": "inox-cmr-central-maddilapalem-vizag-CD1029273",
            "venue_code": "DST_CMRV",
            "address": "CMR Central Mall, Maddilapalem, Visakhapatnam",
            "url": "https://www.district.in/movies/inox-cmr-central-maddilapalem-vizag-CD1029273"
        },
        {
            "name": "INOX: Chitralayaa Mall, Jagadamba, Vizag",
            "slug": "inox-chitralayaa-mall-chitralayaa-vizag-CD1029274",
            "venue_code": "DST_CHIT",
            "address": "Chitralayaa Mall, Suryabagh, Jagadamba, Visakhapatnam",
            "url": "https://www.district.in/movies/inox-chitralayaa-mall-chitralayaa-vizag-CD1029274"
        },
        {
            "name": "AAA Cinemas, Vizag",
            "slug": "aaa-cinemas-vizag-CD1102411",
            "venue_code": "DST_AAAV",
            "address": "Near Railway Station, Visakhapatnam",
            "url": "https://www.district.in/movies/aaa-cinemas-vizag-CD1102411"
        },
        {
            "name": "Asian Mukta A2 Cinemas, VMR Mall, Gajuwaka",
            "slug": "asian-mukta-a2-cinemas-vmr-mall-laser-4k-dolby-atmos-aganampudi-gajuwaka-CD1041782",
            "venue_code": "DST_AM2V",
            "address": "VMR Mall, Aganampudi, Gajuwaka, Visakhapatnam",
            "url": "https://www.district.in/movies/asian-mukta-a2-cinemas-vmr-mall-laser-4k-dolby-atmos-aganampudi-gajuwaka-CD1041782"
        },
        {
            "name": "STBL Cinemas Multiplex SL Nagar, Vizag",
            "slug": "stbl-cinemas-multiplex-sl-nagar-vizag-CD889",
            "venue_code": "DST_STBV",
            "address": "BHPV Post, Sheela Nagar, Visakhapatnam",
            "url": "https://www.district.in/movies/stbl-cinemas-multiplex-sl-nagar-vizag-CD889"
        },
        {
            "name": "Miraj Cinemas : Bhupathi Surya Central, Vizag",
            "slug": "miraj-cinemas-bhupathi-surya-central-visakhapatnam-CD1035674",
            "venue_code": "DST_MIRV",
            "address": "Surya Central, Visakhapatnam",
            "url": "https://www.district.in/movies/miraj-cinemas-bhupathi-surya-central-visakhapatnam-CD1035674"
        },
        {
            "name": "Cinepolis Sreekanya Cineglitz, Madhurwada, Vizag",
            "slug": "cinepolis-sreekanya-cineglitz-madhurwada-vizag-CD9431",
            "venue_code": "DST_SKMV",
            "address": "Madhurwada, Visakhapatnam",
            "url": "https://www.district.in/movies/cinepolis-sreekanya-cineglitz-madhurwada-vizag-CD9431"
        },
        {
            "name": "Kameswari 70mm, RTC Complex Road, Vizag",
            "slug": "kameswari-kinnera-a-c-laser-4k-projection-dolby-atmos-7-1-ultrasound-vizag-CD4000",
            "venue_code": "DST_KAMV",
            "address": "RTC Complex Road, Dwaraka Nagar, Visakhapatnam",
            "url": "https://www.district.in/movies/kameswari-kinnera-a-c-laser-4k-projection-dolby-atmos-7-1-ultrasound-vizag-CD4000"
        },
        {
            "name": "Kinnera 4K Atmos, RTC Complex Road, Vizag",
            "slug": "kameswari-kinnera-a-c-laser-4k-projection-dolby-atmos-7-1-ultrasound-vizag-CD4000",
            "venue_code": "DST_KINV",
            "address": "RTC Complex Road, Dwaraka Nagar, Visakhapatnam",
            "url": "https://www.district.in/movies/kameswari-kinnera-a-c-laser-4k-projection-dolby-atmos-7-1-ultrasound-vizag-CD4000"
        }
    ],

    # --------------------------------------------------------------------------
    # 7. KURNOOL
    # --------------------------------------------------------------------------
    "kurnool": [
        {
            "name": "SVC Cinemas: City Square Mall, Kurnool",
            "slug": "svc-cinemas-city-square-mall-kurnool-CD15527",
            "venue_code": "DST_15527",
            "address": "City Square Mall, Kurnool",
            "url": "https://www.district.in/movies/svc-cinemas-city-square-mall-kurnool-CD15527"
        },
        {
            "name": "Venkatesh Cine Complex: Beside Exhibition Ground",
            "slug": "venkatesh-cine-complex-beside-exhibition-ground-kurnool-CD7312",
            "venue_code": "DST_7312",
            "address": "Beside Exhibition Ground, Kurnool",
            "url": "https://www.district.in/movies/venkatesh-cine-complex-beside-exhibition-ground-kurnool-CD7312"
        },
        {
            "name": "Vijay Theatre: Joharapuram, Kurnool",
            "slug": "vijay-theatre-joharapuram-kurnool-CD7313",
            "venue_code": "DST_7313",
            "address": "Joharapuram, Kurnool",
            "url": "https://www.district.in/movies/vijay-theatre-joharapuram-kurnool-CD7313"
        },
        {
            "name": "Victory Talkies: Minchin Bazar St, Kurnool",
            "slug": "victory-talkies-minchin-bazar-st-marwari-street-kurnool-CD1027251",
            "venue_code": "DST_1027251",
            "address": "Minchin Bazar, Marwari Street, Kurnool",
            "url": "https://www.district.in/movies/victory-talkies-minchin-bazar-st-marwari-street-kurnool-CD1027251"
        },
        {
            "name": "Sri Rama & Sri Krishna Cinemas: Nandikotkur",
            "slug": "sri-rama-sri-krishna-cinemas-nandikotkur-CD1102403",
            "venue_code": "DST_1102403",
            "address": "Nandikotkur, Kurnool",
            "url": "https://www.district.in/movies/sri-rama-sri-krishna-cinemas-nandikotkur-CD1102403"
        }
    ],

    # --------------------------------------------------------------------------
    # 8. HYDERABAD
    # --------------------------------------------------------------------------
    "hyderabad": [
        {
            "name": "Prasads Multiplex: Hyderabad",
            "slug": "prasads-multiplex-hyderabad-CD1028100",
            "venue_code": "DST_PRAS",
            "address": "Khairatabad, Hyderabad",
            "url": "https://www.district.in/movies/prasads-multiplex-hyderabad-CD1028100"
        },
        {
            "name": "AMB Cinemas: Gachibowli",
            "slug": "amb-cinemas-sarath-city-capital-mall-gachibowli-hyderabad-CD1028101",
            "venue_code": "DST_AMBC",
            "address": "Sarath City Capital Mall, Gachibowli, Hyderabad",
            "url": "https://www.district.in/movies/amb-cinemas-sarath-city-capital-mall-gachibowli-hyderabad-CD1028101"
        },
        {
            "name": "AAA Cinemas: Ameerpet",
            "slug": "aaa-cinemas-ameerpet-hyderabad-CD1028102",
            "venue_code": "DST_AAAH",
            "address": "Ameerpet, Hyderabad",
            "url": "https://www.district.in/movies/aaa-cinemas-ameerpet-hyderabad-CD1028102"
        },
        {
            "name": "Sudarshan 35MM: RTC X Roads",
            "slug": "sudarshan-35mm-rtc-x-roads-hyderabad-CD1028103",
            "venue_code": "DST_SUDA",
            "address": "RTC X Roads, Hyderabad",
            "url": "https://www.district.in/movies/sudarshan-35mm-rtc-x-roads-hyderabad-CD1028103"
        },
        {
            "name": "Devi 70MM: RTC X Roads",
            "slug": "devi-70mm-rtc-x-roads-hyderabad-CD1028104",
            "venue_code": "DST_DEVI",
            "address": "RTC X Roads, Hyderabad",
            "url": "https://www.district.in/movies/devi-70mm-rtc-x-roads-hyderabad-CD1028104"
        },
        {
            "name": "Sandhya 70MM: RTC X Roads",
            "slug": "sandhya-70mm-rtc-x-roads-hyderabad-CD1028105",
            "venue_code": "DST_SNDH",
            "address": "RTC X Roads, Hyderabad",
            "url": "https://www.district.in/movies/sandhya-70mm-rtc-x-roads-hyderabad-CD1028105"
        }
    ],

    # --------------------------------------------------------------------------
    # 2. VIJAYAWADA
    # --------------------------------------------------------------------------
    "vijayawada": [
        {
            "name": "Capital Cinemas: Trendset Mall, Vijayawada",
            "slug": "capital-cinemas-trendset-mall-benz-circle-vijayawada-CD1030112",
            "venue_code": "DST_CCTL",
            "address": "Trendset Mall, Benz Circle, Vijayawada",
            "url": "https://www.district.in/movies/capital-cinemas-trendset-mall-benz-circle-vijayawada-CD1030112"
        },
        {
            "name": "Cinepolis: PVP Square Mall, Vijayawada",
            "slug": "cinepolis-pvp-square-mall-mg-road-vijayawada-CD1029105",
            "venue_code": "DST_CPVJ",
            "address": "PVP Square Mall, MG Road, Vijayawada",
            "url": "https://www.district.in/movies/cinepolis-pvp-square-mall-mg-road-vijayawada-CD1029105"
        },
        {
            "name": "ABR Cinemas Neo Screen X: Kanuru, Vijayawada",
            "slug": "abr-cinemas-neo-screen-x-kanuru-vijayawada-CD1030114",
            "venue_code": "DST_ABCR",
            "address": "Kanuru, Vijayawada",
            "url": "https://www.district.in/movies/abr-cinemas-neo-screen-x-kanuru-vijayawada-CD1030114"
        }
    ],

    # --------------------------------------------------------------------------
    # 3. GUNTUR
    # --------------------------------------------------------------------------
    "guntur": [
        {
            "name": "Studio 81 Cinemas: 4K Laser Dolby Atmos, Guntur",
            "slug": "studio-81-cinemas-4k-laser-dolby-atmos-guntur-CD1031101",
            "venue_code": "DST_STTY",
            "address": "Guntur",
            "url": "https://www.district.in/movies/studio-81-cinemas-4k-laser-dolby-atmos-guntur-CD1031101"
        },
        {
            "name": "Harihar Cinemas: Guntur",
            "slug": "harihar-cinemas-guntur-CD1031102",
            "venue_code": "DST_HHCG",
            "address": "Koritepadu, Guntur",
            "url": "https://www.district.in/movies/harihar-cinemas-guntur-CD1031102"
        }
    ],

    # --------------------------------------------------------------------------
    # 4. TIRUPATI
    # --------------------------------------------------------------------------
    "tirupati": [
        {
            "name": "PGR Cinemas A/C 4K Dolby Atmos: Tirupati",
            "slug": "pgr-cinemas-a-c-4k-dolby-atmos-tirupati-CD1032101",
            "venue_code": "DST_PGRC",
            "address": "Tata Nagar, Tirupati",
            "url": "https://www.district.in/movies/pgr-cinemas-a-c-4k-dolby-atmos-tirupati-CD1032101"
        },
        {
            "name": "NVR Jaysyam A/C 4K Dolby Atmos: Tirupati",
            "slug": "nvr-jaysyam-a-c-4k-dolby-atmos-tirupati-CD1032102",
            "venue_code": "DST_JAYD",
            "address": "Tata Nagar, Tirupati",
            "url": "https://www.district.in/movies/nvr-jaysyam-a-c-4k-dolby-atmos-tirupati-CD1032102"
        }
    ],

    # --------------------------------------------------------------------------
    # 5. RAJAHMUNDRY
    # --------------------------------------------------------------------------
    "rajahmundry": [
        {
            "name": "Sarathi Cinemas(Prasaditya Mall):Rajamahendravaram",
            "slug": "sarathi-cinemas-prasaditya-mall-rajamahendravaram-CD1033101",
            "venue_code": "DST_SCPI",
            "address": "Prasaditya Mall, Rajahmundry",
            "url": "https://www.district.in/movies/sarathi-cinemas-prasaditya-mall-rajamahendravaram-CD1033101"
        },
        {
            "name": "Surya Complex Laser RGB 4K Dolby Atmos:Rajahmundry",
            "slug": "surya-complex-laser-rgb-4k-dolby-atmos-rajahmundry-CD1033102",
            "venue_code": "DST_SRYR",
            "address": "Seshayya Metta, Rajahmundry",
            "url": "https://www.district.in/movies/surya-complex-laser-rgb-4k-dolby-atmos-rajahmundry-CD1033102"
        }
    ],

    # --------------------------------------------------------------------------
    # 6. NELLORE
    # --------------------------------------------------------------------------
    "nellore": [
        {
            "name": "Rain Cinema: Nellore",
            "slug": "rain-cinema-nellore-CD1034101",
            "venue_code": "DST_RACN",
            "address": "Rain Square, Dargamitta, Nellore",
            "url": "https://www.district.in/movies/rain-cinema-nellore-CD1034101"
        },
        {
            "name": "Siri Multiplex: Nellore",
            "slug": "siri-multiplex-nellore-CD1034102",
            "venue_code": "DST_JTSM",
            "address": "Ramji Nagar, Nellore",
            "url": "https://www.district.in/movies/siri-multiplex-nellore-CD1034102"
        }
    ],

    # --------------------------------------------------------------------------
    # 9. WARANGAL
    # --------------------------------------------------------------------------
    "warangal": [
        {
            "name": "Asian Sridevi Multiplex: Hanumakonda",
            "slug": "asian-sridevi-multiplex-hanumakonda-CD1035101",
            "venue_code": "DST_ASMW",
            "address": "Hanumakonda, Warangal",
            "url": "https://www.district.in/movies/asian-sridevi-multiplex-hanumakonda-CD1035101"
        },
        {
            "name": "PVR: Warangal, Maddox Mall",
            "slug": "pvr-warangal-maddox-mall-CD1035102",
            "venue_code": "DST_PWLM",
            "address": "Maddox Mall, Girmajipet, Warangal",
            "url": "https://www.district.in/movies/pvr-warangal-maddox-mall-CD1035102"
        }
    ],

    # --------------------------------------------------------------------------
    # 10. KARIMNAGAR
    # --------------------------------------------------------------------------
    "karimnagar": [
        {
            "name": "Asian Paradise Cinemas: Karimnagar",
            "slug": "asian-paradise-cinemas-karimnagar-CD1036101",
            "venue_code": "DST_APCY",
            "address": "Sharma Nagar, Karimnagar",
            "url": "https://www.district.in/movies/asian-paradise-cinemas-karimnagar-CD1036101"
        }
    ],

    # --------------------------------------------------------------------------
    # 11. NIZAMABAD
    # --------------------------------------------------------------------------
    "nizamabad": [
        {
            "name": "PVR: Venu Mall, Nizamabad",
            "slug": "pvr-venu-mall-nizamabad-CD1037101",
            "venue_code": "DST_PRVN",
            "address": "Venu Mall, Nizamabad",
            "url": "https://www.district.in/movies/pvr-venu-mall-nizamabad-CD1037101"
        }
    ],

    # --------------------------------------------------------------------------
    # 12. KHAMMAM
    # --------------------------------------------------------------------------
    "khammam": [
        {
            "name": "Vinoda 4K Dolby Atmos: Khammam",
            "slug": "vinoda-4k-dolby-atmos-khammam-CD1038101",
            "venue_code": "DST_VCKM",
            "address": "Station Road, Khammam",
            "url": "https://www.district.in/movies/vinoda-4k-dolby-atmos-khammam-CD1038101"
        }
    ],

    # --------------------------------------------------------------------------
    # 13. MAHABUBNAGAR
    # --------------------------------------------------------------------------
    "mahabubnagar": [
        {
            "name": "AVD Cinemas: Mahbubnagar",
            "slug": "avd-cinemas-mahbubnagar-CD1039101",
            "venue_code": "DST_AVDM",
            "address": "Shah Saheb Gutta, Mahbubnagar",
            "url": "https://www.district.in/movies/avd-cinemas-mahbubnagar-CD1039101"
        }
    ]
}

# Alias city keys
DISTRICT_THEATER_CATALOG["visakhapatnam"] = DISTRICT_THEATER_CATALOG["vizag"]

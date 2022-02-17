"""
RTCM Protocol payload definitions

Created on 14 Feb 2022

Information sourced from RTCM STANDARD 10403.2 © 2013 RTCM

:author: semuadmin
"""
# pylint: disable=too-many-lines, line-too-long

# *************************************************************
# MSM MESSAGE PAYLOAD DEFINITIONS
# attribute names holding size of MSM repeating groups
NSAT = "NSat"
NSIG = "NSig"
NCELL = "_NCell"
NBIAS = "_NBias"

# MSM message component sections
MSM_HDR = {
    "DF002": "Message number",
    "DF003": "Reference station ID",
    "GNSSEpoch": "GNSS Epoch Time",
    "DF393": "Multiple Message Bit",
    "DF409": "IODS - Issue of Data Station ",
    "DF001_7": "Reserved",
    "DF411": "Clock Steering Indicator",
    "DF412": "External Clock Indicator",
    "DF417": "GNSS Divergence-free Smoothing Indicator",
    "DF418": "GNSS Smoothing Interval",
    "DF394": "GNSS Satellite Mask ",  # NSAT = num of set bits
    "DF395": "GNSS Signal Mask ",  # NSIG = num of set bits
    "DF396": "GNSS Cell Mask ",  # size = NCELL = NSAT * NSIG
}

MSM_SAT_123 = {
    "group": (
        NSAT,
        {
            "DF398": "GNSS Satellite rough ranges modulo 1 millisecond",
        },
    ),
}

MSM_SAT_46 = {
    "group1": (
        NSAT,
        {
            "DF397": "Number of int millisecs in GNSS Satellite roughranges",
        },
    ),
    "group2": (
        NSAT,
        {
            "DF398": "GNSS Satellite rough ranges modulo 1 millisecond",
        },
    ),
}


MSM_SAT_57 = {
    "group1": (
        NSAT,
        {
            "DF397": "The number of integer milliseconds in GNSS Satellite rough ranges",
        },
    ),
    "group2": (
        NSAT,
        {
            "GNSSSpecific": "Extended Satellite Information",
        },
    ),
    "group3": (
        NSAT,
        {
            "DF398": "GNSS Satellite rough ranges modulo 1 millisecond",
        },
    ),
    "group4": (
        NSAT,
        {
            "DF399": "GNSS Satellite rough PhaseRangeRates ",
        },
    ),
}


MSM_SIG_1 = {
    "group1": (
        NCELL,
        {
            "DF400": "GNSS signal fine Pseudoranges",
        },
    ),
}

MSM_SIG_2 = {
    "group1": (
        NCELL,
        {
            "DF401": "GNSS signal fine PhaseRange data",
        },
    ),
    "group2": (
        NCELL,
        {
            "DF402": "GNSS PhaseRange Lock",
        },
    ),
    "group3": (
        NCELL,
        {
            "DF420",
            "Half-cycle ambiguity indicator",
        },
    ),
}

MSM_SIG_3 = {
    "group1": (
        NCELL,
        {
            "DF400": "GNSS signal fine Pseudoranges",
        },
    ),
    "group2": (
        NCELL,
        {
            "DF401": "GNSS signal fine PhaseRange data",
        },
    ),
    "group3": (
        NCELL,
        {
            "DF402": "GNSS PhaseRange Lock",
        },
    ),
    "group4": (
        NCELL,
        {
            "DF420": "Half-cycle ambiguity indicator",
        },
    ),
}

MSM_SIG_4 = {
    "group1": (
        NCELL,
        {
            "DF400": "GNSS signal fine Pseudoranges",
        },
    ),
    "group2": (
        NCELL,
        {
            "DF401": "GNSS signal fine PhaseRange data",
        },
    ),
    "group3": (
        NCELL,
        {
            "DF402": "GNSS PhaseRange Lock",
        },
    ),
    "group4": (
        NCELL,
        {
            "DF420": "Half-cycle ambiguity indicator",
        },
    ),
    "group5": (
        NCELL,
        {
            "DF403": "GNSS signal CNRs",
        },
    ),
}

MSM_SIG_5 = {
    "group1": (
        NCELL,
        {
            "DF400": "GNSS signal fine Pseudoranges",
        },
    ),
    "group2": (
        NCELL,
        {
            "DF401": "GNSS signal fine PhaseRange data",
        },
    ),
    "group3": (
        NCELL,
        {
            "DF402": "GNSS PhaseRange Lock",
        },
    ),
    "group4": (
        NCELL,
        {
            "DF420": "Half-cycle ambiguity indicator",
        },
    ),
    "group5": (
        NCELL,
        {
            "DF403": "GNSS signal CNRs",
        },
    ),
    "group6": (
        NCELL,
        {
            "DF404": "GNSS signal fine PhaseRangeRates ",
        },
    ),
}

MSM_SIG_6 = {
    "group1": (
        NCELL,
        {
            "DF405": "GNSS signal fine",
        },
    ),
    "group2": (
        NCELL,
        {
            "DF406": "GNSS signal fine PhaseRange data with extended resolution",
        },
    ),
    "group3": (
        NCELL,
        {
            "DF407": "GNSS PhaseRange Lock",
        },
    ),
    "group4": (
        NCELL,
        {
            "DF420": "Half-cycle ambiguity indicator",
        },
    ),
    "group5": (
        NCELL,
        {
            "DF408": "GNSS signal CNRs with extended resolution",
        },
    ),
}

MSM_SIG_7 = {
    "group1": (
        NCELL,
        {
            "DF405": "GNSS signal fine",
        },
    ),
    "group2": (
        NCELL,
        {
            "DF406": "GNSS signal fine PhaseRange data with extended resolution",
        },
    ),
    "group3": (
        NCELL,
        {
            "DF407": "GNSS PhaseRange Lock",
        },
    ),
    "group4": (
        NCELL,
        {
            "DF420": "Half-cycle ambiguity indicator",
        },
    ),
    "group5": (
        NCELL,
        {
            "DF408": "GNSS signal CNRs with extended resolution",
        },
    ),
    "group6": (
        NCELL,
        {
            "DF404": "GNSS signal fine PhaseRangeRates",
        },
    ),
}

# concatenate MSM sections in to a single dict
# NB: Python >=3.9 supports the more intuitive | (union)
# operation for this, but earlier versions don't.
MSM1 = {**MSM_HDR, **MSM_SAT_123, **MSM_SIG_1}
MSM2 = {**MSM_HDR, **MSM_SAT_123, **MSM_SIG_2}
MSM3 = {**MSM_HDR, **MSM_SAT_123, **MSM_SIG_3}
MSM4 = {**MSM_HDR, **MSM_SAT_46, **MSM_SIG_4}
MSM5 = {**MSM_HDR, **MSM_SAT_57, **MSM_SIG_5}
MSM6 = {**MSM_HDR, **MSM_SAT_46, **MSM_SIG_6}
MSM7 = {**MSM_HDR, **MSM_SAT_57, **MSM_SIG_7}
# *************************************************************

RTCM_PAYLOADS_GET = {
    "1001": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF004": "GPS Epoch Time (TOW) ",
        "DF005": "Synchronous GNSS Flag",
        "DF006": "No. of GPS Satellite Signals Processed",
        "DF007": "GPS Divergence-free Smoothing Indicator",
        "DF008": "GPS Smoothing Interval",
        "group": (  # repeating group * DF006
            "DF006",
            {
                "DF009": "GPS Satellite ID",
                "DF010": "GPS L1 Code Indicator",
                "DF011": "GPS L1 Pseudorange",
                "DF012": "GPS L1 PhaseRange - L1 Pseudorange ",
                "DF013": "GPS L1 Lock time Indicator",
            },
        ),
    },
    "1002": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF004": "GPS Epoch Time (TOW) ",
        "DF005": "Synchronous GNSS Flag",
        "DF006": "No. of GPS Satellite Signals Processed",
        "DF007": "GPS Divergence-free Smoothing Indicator",
        "DF008": "GPS Smoothing Interval",
        "group": (  # repeating group * DF006
            "DF006",
            {
                "DF009": "GPS Satellite ID",
                "DF010": "GPS L1 Code Indicator",
                "DF011": "GPS L1 Pseudorange",
                "DF012": "GPS L1 PhaseRange - L1 Pseudorange ",
                "DF013": "GPS L1 Lock time Indicator",
                "DF014": "GPS Integer L1 Pseudorange Modulus Ambiguity",
                "DF015": "GPS L1 CNR",
            },
        ),
    },
    "1003": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF004": "GPS Epoch Time (TOW) ",
        "DF005": "Synchronous GNSS Flag",
        "DF006": "No. of GPS Satellite Signals Processed",
        "DF007": "GPS Divergence-free Smoothing Indicator",
        "DF008": "GPS Smoothing Interval",
        "group": (  # repeating group * DF006
            "DF006",
            {
                "DF009": "GPS Satellite ID",
                "DF010": "GPS L1 Code Indicator",
                "DF011": "GPS L1 Pseudorange",
                "DF012": "GPS L1 PhaseRange - L1 Pseudorange ",
                "DF013": "GPS L1 Lock time Indicator",
                "DF016": "GPS L2 Code Indicator",
                "DF017": "GPS L2-L1 Pseudorange Difference",
                "DF018": "GPS L2 PhaseRange - L1 Pseudorange ",
                "DF019": "GPS L2 Lock time Indicator",
            },
        ),
    },
    "1004": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF004": "GPS Epoch Time (TOW) ",
        "DF005": "Synchronous GNSS Flag",
        "DF006": "No. of GPS Satellite Signals Processed",
        "DF007": "GPS Divergence-free Smoothing Indicator",
        "DF008": "GPS Smoothing Interval",
        "group": (  # repeating group * DF006
            "DF006",
            {
                "DF009": "GPS Satellite ID",
                "DF010": "GPS L1 Code Indicator",
                "DF011": "GPS L1 Pseudorange",
                "DF012": "GPS L1 PhaseRange - L1 Pseudorange ",
                "DF013": "GPS L1 Lock time Indicator",
                "DF014": "GPS Integer L1 Pseudorange Modulus Ambiguity",
                "DF015": "GPS L1 CNR",
                "DF016": "GPS L2 Code Indicator",
                "DF017": "GPS L2-L1 Pseudorange Difference",
                "DF018": "GPS L2 PhaseRange - L1 Pseudorange ",
                "DF019": "GPS L2 Lock time Indicator",
                "DF020": "GPS L2 CNR",
            },
        ),
    },
    "1005": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF021": "Reserved for ITRF Realization Year",
        "DF022": "GPS Indicator",
        "DF023": "GLONASS Indicator",
        "DF024": "Reserved for Galileo Indicator",
        "DF141": "Reference-Station Indicator",
        "DF025": "Antenna Reference Point ECEF-X",
        "DF142": "Single Receiver Oscillator Indicator",
        "DF001_1": "Reserved",
        "DF026": "Antenna Reference Point ECEF-Y",
        "DF001_2": "Reserved",
        "DF027": "Antenna Reference Point ECEF-Z",
    },
    "1006": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF021": "Reserved for ITRF Realization Year",
        "DF022": "GPS Indicator",
        "DF023": "GLONASS Indicator",
        "DF024": "Reserved for Galileo Indicator",
        "DF141": "Reference-Station Indicator",
        "DF025": "Antenna Reference Point ECEF-X",
        "DF142": "Single Receiver Oscillator Indicator",
        "DF001_1": "Reserved",
        "DF026": "Antenna Reference Point ECEF-Y",
        "DF001_2": "Reserved",
        "DF027": "Antenna Reference Point ECEF-Z",
        "DF028": "Antenna Height",
    },
    "1007": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF029": "Descriptor Counter N",
        "group": (  # repeating group * DF029
            "DF029",
            {
                "DF030": "Antenna Descriptor",
            },
        ),
        "DF031": "Antenna Setup ID",
    },
    "1008": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF029": "Descriptor Counter N",
        "group_1": (  # repeating group * DF029
            "DF029",
            {
                "DF030": "Antenna Descriptor",
            },
        ),
        "DF031": "Antenna Setup ID",
        "DF032": "Serial Number Counter M",
        "group_2": (  # repeating group * DF032
            "DF032",
            {
                "DF033": "Antenna Serial Number",
            },
        ),
    },
    "1009": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF034": "GLONASS Epoch Time (tk) ",
        "DF005": "Synchronous GNSS Flag",
        "DF035": "No. of GLONASS Satellite Signals Processed",
        "DF036": "GLONASS Divergence-free Smoothing Indicator",
        "DF037": "GLONASS Smoothing Interval",
        "group": (  # repeating group * DF035
            "DF035",
            {
                "DF038": "GLONASS Satellite ID (Satellite Slot Number)",
                "DF039": "GLONASS Code Indicator",
                "DF040": "GLONASS Satellite Frequency Channel Number",
                "DF041": "GLONASS L1 Pseudorange",
                "DF042": "GLONASS L1 PhaseRange - L1 Pseudorange ",
                "DF043": "GLONASS L1 Lock time Indicator",
            },
        ),
    },
    "1010": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF034": "GLONASS Epoch Time (tk) ",
        "DF005": "Synchronous GNSS Flag",
        "DF035": "No. of GLONASS Satellite Signals Processed",
        "DF036": "GLONASS Divergence-free Smoothing Indicator",
        "DF037": "GLONASS Smoothing Interval",
        "group": (  # repeating group * DF035
            "DF035",
            {
                "DF038": "GLONASS Satellite ID (Satellite Slot Number)",
                "DF039": "GLONASS L1 Code Indicator",
                "DF040": "GLONASS Satellite Frequency Channel Number",
                "DF041": "GLONASS L1 Pseudorange",
                "DF042": "GLONASS L1 PhaseRange - L1 Pseudorange ",
                "DF043": "GLONASS L1 Lock time Indicator",
                "DF044": "GLONASS Integer L1 Pseudorange Modulus Ambiguity",
                "DF045": "GLONASS L1 CNR",
            },
        ),
    },
    "1011": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF034": "GLONASS Epoch Time (tk) ",
        "DF005": "Synchronous GNSS Flag",
        "DF035": "No. of GLONASS Satellite Signals Processed",
        "DF036": "GLONASS Divergence-free Smoothing Indicator",
        "DF037": "GLONASS Smoothing Interval",
        "group": (  # repeating group * DF035
            "DF035",
            {
                "DF038": "GLONASS Satellite ID (Satellite Slot Number)",
                "DF039": "GLONASS L1 Code Indicator",
                "DF040": "GLONASS Satellite Frequency Channel Number",
                "DF041": "GLONASS L1 Pseudorange",
                "DF042": "GLONASS L1 PhaseRange - L1 Pseudorange ",
                "DF043": "GLONASS L1 Lock time Indicator",
                "DF046": "GLONASS L2 Code Indicator",
                "DF047": "GLONASS L2-L1 Pseudorange Difference",
                "DF048": "GLONASS L2 PhaseRange - L1 Pseudorange ",
                "DF049": "GLONASS L2 Lock time Indicator",
            },
        ),
    },
    "1012": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF034": "GLONASS Epoch Time (tk) ",
        "DF005": "Synchronous GNSS Flag",
        "DF035": "No. of GLONASS Satellite Signals Processed",
        "DF036": "GLONASS Divergence-free Smoothing Indicator",
        "DF037": "GLONASS Smoothing Interval",
        "group": (  # repeating group * DF035
            "DF035",
            {
                "DF038": "GLONASS Satellite ID (Satellite Slot Number)",
                "DF039": "GLONASS L1 Code Indicator",
                "DF040": "GLONASS Satellite Frequency Channel Number",
                "DF041": "GLONASS L1 Pseudorange",
                "DF042": "GLONASS L1 PhaseRange - L1 Pseudorange ",
                "DF043": "GLONASS L1 Lock time Indicator",
                "DF044": "GLONASS Integer L1 Pseudorange Modulus Ambiguity ",
                "DF045": "GLONASS L1 CNR",
                "DF046": "GLONASS L2 Code Indicator",
                "DF047": "GLONASS L2-L1 Pseudorange Difference",
                "DF048": "GLONASS L2 PhaseRange - L1 Pseudorange ",
                "DF049": "GLONASS L2 Lock time Indicator",
                "DF050": "GLONASS L2 CNR",
            },
        ),
    },
    "1013": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF051": "Modified Julian Day (MJD) Number",
        "DF052": "Seconds of Day (UTC)",
        "DF053": "No. of Message ID Announcements to Follow (Nm)",
        "DF054": "Leap Seconds, GPS-UTC",
        "group": (  # repeating group * DF053
            "DF053",
            {
                "DF055": "Message ID",
                "DF056": "Message Sync Flag",
                "DF057": "Message Transmission Interval",
            },
        ),
    },
    "1014": {
        "DF002": "Message Identity",
        "DF059": "Network ID",
        "DF072": "Subnetwork ID",
        "DF058": "Number of Auxiliary Stations Transmitted",
        "DF060": "Master Reference Station ID",
        "DF061": "Auxiliary Reference Station ID",
        "DF062": "Aux-Master Delta Latitude",
        "DF063": "Aux-Master Delta Longitude",
        "DF064": "Aux-Master Delta Height",
    },
    "1015": {
        "DF002": "Message Identity",
        "DF059": "Network ID",
        "DF072": "Subnetwork ID",
        "DF065": "GPS Epoch Time (GPS TOW)",
        "DF066": "GPS Multiple Message Indicator ",
        "DF060": "Master Reference Station ID",
        "DF061": "Auxiliary Reference Station ID ",
        "DF067": "# of GPS Sats",
        "group": (  # repeating group * DF067
            "DF067",
            {
                "DF068": "GPS Satellite ID",
                "DF074": "GPS Ambiguity Status Flag",
                "DF075": "GPS Non Sync Count",
                "DF069": "GPS Ionospheric Carrier Phase Correction Difference",
            },
        ),
    },
    "1016": {
        "DF002": "Message Identity",
        "DF059": "Network ID",
        "DF072": "Subnetwork ID",
        "DF065": "GPS Epoch Time (GPS TOW)",
        "DF066": "GPS Multiple Message Indicator ",
        "DF060": "Master Reference Station ID",
        "DF061": "Auxiliary Reference Station ID ",
        "DF067": "# of GPS Sats",
        "group": (  # repeating group * DF067
            "DF067",
            {
                "DF068": "GPS Satellite ID",
                "DF074": "GPS Ambiguity Status Flag",
                "DF075": "GPS Non Sync Count",
                "DF070": "GPS Geometric Carrier Phase Correction Difference",
                "DF071": "GPS IODE",
            },
        ),
    },
    "1017": {
        "DF002": "Message Identity",
        "DF059": "Network ID",
        "DF072": "Subnetwork ID",
        "DF065": "GPS Epoch Time (GPS TOW)",
        "DF066": "GPS Multiple Message Indicator ",
        "DF060": "Master Reference Station ID",
        "DF061": "Auxiliary Reference Station ID ",
        "DF067": "# of GPS Sats",
        "group": (  # repeating group * DF067
            "DF067",
            {
                "DF068": "GPS Satellite ID",
                "DF074": "GPS Ambiguity Status Flag",
                "DF075": "GPS Non Sync Count",
                "DF070": "GPS Geometric Carrier Phase Correction Difference",
                "DF071": "GPS IODE",
                "DF069": "GPS Ionospheric Carrier Phase Correction Difference",
            },
        ),
    },
    "1019": {
        "DF002": "Message Identity",
        "DF009": "GPS Satellite ID",
        "DF076": "GPS Week Number",
        "DF077": "GPS SV ACCURACY",
        "DF078": "GPS CODE ON L2",
        "DF079": "GPS IDOT",
        "DF071": "GPS IODE",
        "DF081": "GPS toc",
        "DF082": "GPS af2",
        "DF083": "GPS af1",
        "DF084": "GPS af0",
        "DF085": "GPS IODC",
        "DF086": "GPS Crs",
        "DF087": "GPS Δn (DELTA n)",
        "DF088": "GPS M0",
        "DF089": "GPS Cuc",
        "DF090": "GPS Eccentricity (e)",
        "DF091": "GPS Cus",
        "DF092": "GPS (A)1/2",
        "DF093": "GPS toe",
        "DF094": "GPS Cic",
        "DF095": "GPS Ω0 (OMEGA)0",
        "DF096": "GPS Cis",
        "DF097": "GPS i0",
        "DF098": "GPS Crc",
        "DF099": "GPS ω (Argument of Perigee)",
        "DF100": "GPS OMEGADOT (Rate of Right Ascension)",
        "DF101": "GPS tGD",
        "DF102": "GPS SV HEALTH",
        "DF103": "GPS L2 P data flag",
        "DF137": "GPS Fit Interval",
    },
    "1020": {
        "DF002": "Message Identity",
        "DF038": "GLONASS Satellite ID (Satellite Slot Number)",
        "DF040": "GLONASS Satellite Frequency Channel Number",
        "DF104": "GLONASS almanac health (Cn word)",
        "DF105": "GLONASS almanac health availability indicator",
        "DF106": "GLONASS P1",
        "DF107": "GLONASS tk",
        "DF108": "GLONASS MSB of Bn word",
        "DF109": "GLONASS P2",
        "DF110": "GLONASS tb",
        "DF111": "GLONASS xn(tb), first derivative",
        "DF112": "GLONASS xn(tb)",
        "DF113": "GLONASS xn(tb), second derivative",
        "DF114": "GLONASS yn(tb), first derivative",
        "DF115": "GLONASS yn(tb)",
        "DF116": "GLONASS yn(tb), second derivative",
        "DF117": "GLONASS zn(tb), first derivative",
        "DF118": "GLONASS zn(tb)",
        "DF119": "GLONASS zn(tb), second derivative",
        "DF120": "GLONASS P3",
        "DF121": "GLONASS yn(tb)",
        "DF122": "GLONASS-M P",
        "DF123": "GLONASS-M ln  (third string)",
        "DF124": "GLONASS τn(tb)",
        "DF125": "GLONASS-M Δτn",
        "DF126": "GLONASS En",
        "DF127": "GLONASS-M P4",
        "DF128": "GLONASS-M FT",
        "DF129": "GLONASS-M NT",
        "DF130": "GLONASS-M M",
        "DF131": "GLONASS The Availability of Additional Data",
        "DF132": "GLONASS NA",
        "DF133": "GLONASS τc",
        "DF134": "GLONASS-M N4",
        "DF135": "GLONASS-M τGPS",
        "DF136": "GLONASS-M ln (fifth string)",
    },
    "1029": {
        "DF002": "Message Identity",
        "DF003": "Reference Station ID",
        "DF051": "Modified Julian Day (MJD) Number",
        "DF052": "Seconds of Day (UTC)",
        "DF138": "Number of Characters to Follow",
        "DF139": "Number of UTF-8 Code Units (N)",
        "group": (  # repeating group * DF139
            "DF139",
            {
                "DF140": "UTF-8 Character Code Units",
            },
        ),
    },
    "1027": {
        "DF002": "Message Number ",
        "DF147": "System Identification Number",
        "DF170": "Projection Type",
        "DF182": "Rectification Flag",
        "DF183": "LaPC - Latitude of Projection Center",
        "DF184": "LoPC - Longitude of Projection Center",
        "DF185": "AzIL - Azimuth of Initial Line",
        "DF186": "Diff ARSG - Difference, Angle from Rectified to Skew Grid",
        "DF187": "Add SIL - Scale factor on Initial Line",
        "DF188": "EPC - Easting at Projection Center",
        "DF189": "NPC - Northing at Projection Center",
    },
    # GPS
    "1071": MSM1,
    "1072": MSM2,
    "1073": MSM3,
    "1074": MSM4,
    "1075": MSM5,
    "1076": MSM6,
    "1077": MSM7,
    # GLONASS
    "1081": MSM1,
    "1082": MSM2,
    "1083": MSM3,
    "1084": MSM4,
    "1085": MSM5,
    "1086": MSM6,
    "1087": MSM7,
    # Galileo
    "1091": MSM1,
    "1092": MSM2,
    "1093": MSM3,
    "1094": MSM4,
    "1095": MSM5,
    "1096": MSM6,
    "1097": MSM7,
    # QZSS
    "1111": MSM1,
    "1112": MSM2,
    "1113": MSM3,
    "1114": MSM4,
    "1115": MSM5,
    "1116": MSM6,
    "1117": MSM7,
    # BeiDou
    "1121": MSM1,
    "1122": MSM2,
    "1123": MSM3,
    "1124": MSM4,
    "1125": MSM5,
    "1126": MSM6,
    "1127": MSM7,
    "1230": {
        "DF002": "Message Number",
        "DF003": "Reference Station ID",
        "DF421": "GLONASS Code-Phase bias indicator",
        "DF001_3": "Reserved",
        "DF422": "GLONASS FDMA signals mask",  # _NBias = num bits set
        "group": (
            NBIAS,  # TODO does this only ever contain one grouped bias?
            {
                "DF423": "GLONASS L1 C/A Code-Phase Bias",
                # "DF424": "GLONASS L1 P Code-Phase Bias",
                # "DF425": "GLONASS L2 C/A Code-Phase Bias",
                # "DF426": "GLONASS L2 P Code-Phase Bias",
            },
        ),
    },
}

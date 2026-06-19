def combine(
dcf,
pe,
ddm,
monte
):


    weights={

    "dcf":0.4,

    "pe":0.25,

    "ddm":0.1,

    "monte":0.25

    }


    return (
    dcf*weights["dcf"]
    +
    pe*weights["pe"]
    +
    ddm*weights["ddm"]
    +
    monte*weights["monte"]
    )
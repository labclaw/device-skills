# teready, te1ready, te2ready, te3ready, te4ready

**Category:** Commands > Acquire > Sample

## NAME

**teready** - Waiting command to ensure the desired temperature TE is stable

**te1ready** - Waiting command to ensure the desired temperature TE1 on VPSB board channel 1 is stable

**te2ready** - Waiting command to ensure the desired temperature TE2 on VPSB board channel 2 is stable

**te3ready** - Waiting command to ensure the desired temperature TE3 on VPSB board channel 3 is stable

**te4ready** - Waiting command to ensure the desired temperature TE4 on VPSB board channel 4 is stable


## DESCRIPTION

The teready command waits waittime seconds to ensure a temperature stability with the specified accuracy. First, the temperature must be reached with the accuracy degree for 10 seconds, then the waittime period will be added to ensure stability. This is particularly useful in AU programs and automation in general when different samples are to be measured at different temperatures. The teready commands make sure that the data acquisition is only started once the desired temperature has been reached and is stable.


## USAGE IN AU PROGRAMS

1. TEREADY
2. TE1READY
3. TE2READY
4. TE3READY
5. TE3READY
© 2025 Bruker BioSpin GmbH & Co. KG

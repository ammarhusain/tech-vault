#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

usage() {
    cat <<EOF
Usage: devices [OPTIONS]

Options:
    --all         Show all devices, including those deprecated in current SDK
    --deprecated  Show only devices deprecated in current SDK
    --sdk <sdk>   Use custom SDK for query (default: all)
EOF
}

DEPRECATED=False
SDKS=(macosx iphoneos appletvos watchos xros)

while [[ $# -gt 0 ]]; do
    case $1 in
    --deprecated)
        DEPRECATED=True
        ;;
    --sdk)
        SDKS=("$2")
        shift
        ;;
    *)
        usage
        exit 1
        ;;
    esac
    shift
done

for SDK in ${SDKS[@]}; do
    QUERY=$(cat << EOQ
        SELECT DISTINCT
            Platform,
            PlatformName as Chip,
            COALESCE(NULLIF(GPUPipeline,""), "N/A") as Chip2,
            GFXFirmwareType as Chip3,
            TargetTypeMixed as Device,
            ProductType,
            ProductDescription,
            ArtworkDisplayGamut as Gamut

        FROM
            Targets

        WHERE
            SDKPlatform == "${SDK}"
            AND ArtworkDisplayGamut <> ""

        ORDER BY
            Platform,
            Device

EOQ
    )

    echo ${SDK}
    echo "-----------------------"
    xcrun --sdk ${SDK}.internal embedded_device_map -header -query "${QUERY}" \
        | column -t -s '|'
    echo
done
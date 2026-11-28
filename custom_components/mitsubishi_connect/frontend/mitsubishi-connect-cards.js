const DOMAIN = "mitsubishi_connect";

const ROLES = {
  lock: { domain: "button", key: "lock_doors", suffixes: ["lock_doors"] },
  unlock: { domain: "button", key: "unlock_doors", suffixes: ["unlock_doors"] },
  lights: { domain: "button", key: "flash_lights", suffixes: ["flash_lights"] },
  horn: { domain: "button", key: "sound_horn", suffixes: ["sound_horn"] },
  refresh: { domain: "button", key: "force_refresh", suffixes: ["refresh_vehicle_status", "force_refresh"] },
  locate: { domain: "button", key: "update_location", suffixes: ["update_gps_location", "update_location"] },
  tracker: { domain: "device_tracker", key: "location", suffixes: ["location"] },
  start_engine: { domain: "button", key: "start_engine", suffixes: ["start_engine"] },
  stop_engine: { domain: "button", key: "stop_engine", suffixes: ["stop_engine"] },
  engine: { domain: "binary_sensor", key: "engine_running", suffixes: ["engine"] },
  temperature: { domain: "number", key: "remote_start_temp", suffixes: ["remote_start_temperature"] },
  cabin_target: { domain: "sensor", key: "target_cabin_temp", suffixes: ["target_cabin_temperature"] },
  range: { domain: "sensor", key: "fuel_range", suffixes: ["fuel_range"] },
  odometer: { domain: "sensor", key: "odometer", suffixes: ["odometer"] },
  updated: { domain: "sensor", key: "last_telemetry_update", suffixes: ["last_telemetry_update"] },
  front_defrost: { domain: "switch", key: "hvac_front_defrost", suffixes: ["remote_start_front_defrost", "front_defrost"] },
  rear_defrost: { domain: "switch", key: "hvac_rear_defrost", suffixes: ["remote_start_rear_defrost", "rear_defrost"] },
  steering_heater: { domain: "switch", key: "hvac_steering_heater", suffixes: ["remote_start_steering_wheel_heater", "steering_wheel_heater"] },
  headlights: { domain: "binary_sensor", key: "headlights", suffixes: ["headlights"] },
  brake_warning: { domain: "binary_sensor", key: "brake_warning", suffixes: ["brake_warning"] },
  oil_warning: { domain: "binary_sensor", key: "engine_oil_warning", suffixes: ["engine_oil_warning"] },
  door_fl: { domain: "binary_sensor", key: "front_left_door", suffixes: ["front_left_door"] },
  door_fr: { domain: "binary_sensor", key: "front_right_door", suffixes: ["front_right_door"] },
  door_rl: { domain: "binary_sensor", key: "rear_left_door", suffixes: ["rear_left_door"] },
  door_rr: { domain: "binary_sensor", key: "rear_right_door", suffixes: ["rear_right_door"] },
  hood: { domain: "binary_sensor", key: "hood", suffixes: ["hood"] },
  trunk: { domain: "binary_sensor", key: "trunk", suffixes: ["trunk"] },
  fuel_level: { domain: "sensor", key: "fuel_level", suffixes: [] },
  battery: { domain: "sensor", key: "battery_level", suffixes: [] },
  ev_range: { domain: "sensor", key: "ev_range", suffixes: [] },
  charging: { domain: "switch", key: "charging", suffixes: [] },
};

const OPENINGS = ["door_fl", "door_fr", "door_rl", "door_rr", "hood", "trunk"];

const TEXT = {
  fr: {
    sep: " : ", parked: "Stationné", running: "Moteur en marche", updated: "Données", never: "jamais actualisé",
    lock: "Verrouiller", unlock: "Ouvrir", start: "Démarrer", stop: "Arrêter", lights: "Phares", horn: "Klaxon",
    climate: "Climat", location: "Localisation", openings: "Ouvrants", odometer: "Odomètre", charging: "Recharge",
    allClosed: "Portes, capot et hayon fermés", open: "ouvert", unknown: "État inconnu",
    door_fl: "Porte AV G", door_fr: "Porte AV D", door_rl: "Porte AR G", door_rr: "Porte AR D", hood: "Capot", trunk: "Hayon",
    windowsOpen: "vitre(s) ouverte(s)", warnings: "Alertes", brake_warning: "Freins", oil_warning: "Huile moteur",
    target: "Cible", presetsNote: "Réglages appliqués au prochain démarrage à distance",
    front_defrost: "Dégivrage avant", rear_defrost: "Dégivrage arrière", steering_heater: "Volant chauffant",
    startWith: "Démarrer avec ces réglages", stopEngine: "Arrêter le moteur",
    confirm: "Confirmer", cancel: "Annuler", holdToStart: "Maintenir pour démarrer",
    confirmUnlock: "Déverrouiller les portes ?", confirmUnlockText: "La commande part vers le véhicule.",
    confirmStart: "Démarrer le moteur à distance ?", confirmStartText: "Portes, capot et hayon fermés, portes verrouillées. Jamais dans un garage fermé.", blocked: "sera refusé par le véhicule",
    sending: "Envoi au véhicule…", done: "Commande confirmée", failed: "Échec",
    locate: "Actualiser la position", refresh: "Actualiser l'état", battery: "Batterie", evRange: "élec.",
    charge: "Charger", noDevice: "Aucun véhicule Mitsubishi Connect trouvé",
    pressed: { lock: "Portes verrouillées", unlock: "Portes déverrouillées", lights: "Phares clignotés", horn: "Klaxon déclenché", refresh: "État actualisé", locate: "Position actualisée", engine_on: "Moteur démarré", engine_off: "Moteur arrêté", charging_on: "Recharge démarrée", charging_off: "Recharge arrêtée" },
  },
  en: {
    sep: ": ", parked: "Parked", running: "Engine running", updated: "Data", never: "never refreshed",
    lock: "Lock", unlock: "Unlock", start: "Start", stop: "Stop", lights: "Lights", horn: "Horn",
    climate: "Climate", location: "Location", openings: "Openings", odometer: "Odometer", charging: "Charging",
    allClosed: "Doors, hood and tailgate closed", open: "open", unknown: "Unknown",
    door_fl: "Front left door", door_fr: "Front right door", door_rl: "Rear left door", door_rr: "Rear right door", hood: "Hood", trunk: "Tailgate",
    windowsOpen: "window(s) open", warnings: "Warnings", brake_warning: "Brakes", oil_warning: "Engine oil",
    target: "Target", presetsNote: "Settings apply to the next remote start",
    front_defrost: "Front defrost", rear_defrost: "Rear defrost", steering_heater: "Heated wheel",
    startWith: "Start with these settings", stopEngine: "Stop engine",
    confirm: "Confirm", cancel: "Cancel", holdToStart: "Hold to start",
    confirmUnlock: "Unlock the doors?", confirmUnlockText: "The command is sent to the vehicle.",
    confirmStart: "Remote start the engine?", confirmStartText: "Doors, hood and tailgate closed, doors locked. Never in a closed garage.", blocked: "the vehicle will refuse to start",
    sending: "Sending to vehicle…", done: "Command confirmed", failed: "Failed",
    locate: "Refresh location", refresh: "Refresh status", battery: "Battery", evRange: "EV",
    charge: "Charge", noDevice: "No Mitsubishi Connect vehicle found",
    pressed: { lock: "Doors locked", unlock: "Doors unlocked", lights: "Lights flashed", horn: "Horn sounded", refresh: "Status refreshed", locate: "Location refreshed", engine_on: "Engine started", engine_off: "Engine stopped", charging_on: "Charging started", charging_off: "Charging stopped" },
  },
};

const PAINTS = {
  blanc: { hi: "#ffffff", mid: "#f3f2ee", hz: "#9ea3a8", bo: "#e6e4df", low: "#cdcbc6", deep: "#7f8389" },
  titane: { hi: "#f2f5f7", mid: "#a7aeb5", hz: "#3c4249", bo: "#8c939a", low: "#5b6269", deep: "#23272b" },
  noir: { hi: "#a3acb5", mid: "#3b4148", hz: "#0a0b0d", bo: "#30353b", low: "#1b1e22", deep: "#08090a" },
  rouge: { hi: "#ffa3a3", mid: "#cf2638", hz: "#55060f", bo: "#b81b2d", low: "#8b0c1c", deep: "#36040a" },
  bleu: { hi: "#b9d3f2", mid: "#3f6d9e", hz: "#0f2135", bo: "#335c88", low: "#1f3d5e", deep: "#0b1724" },
};

const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
let uidSeq = 0;

function carSvg({ paint, roofBlack, open, lit, aria, u }) {
  const p = PAINTS[paint] || PAINTS.blanc;
  const beam = lit ? 0.95 : 0;
  const tailGlow = lit ? 0.8 : 0;
  const roofO = roofBlack ? 1 : 0;
  const drl = lit ? "#ffffff" : "#dde5ec";
  const lamp = lit ? "#fff6d6" : "#9aa4ae";
  const tailHi = lit ? "#ff6b7a" : "#e0283c";
  const tailLo = lit ? "#d10f27" : "#7a0814";
  const gateT = open ? "rotate(68 98 28)" : "rotate(0 98 28)";
  const dlo = "M337 73.5 L160 70.5 C135 70 120 67 106 60 L103 40 C106 36.5 112 35 122 34.5 L262 34 C272 34 280 35.5 286 39 C304 50 322 62 337 73.5 Z";
  const body = "M36 151 C32 144 30.5 132 30.5 116 C30.5 100 31 84 33 71 C42 62 56 50 66 38 L84 28 C100 27 116 27 132 27 L232 27.5 C250 28 262 29.5 274 33 C296 44 322 60 343 71 C372 73 410 75.5 432 80 C442 83 450 90 454 98 C458 106 460 118 459 128 C458 140 456 150 451 155 L421 153 A41 41 0 0 0 339 153 L159 153 A41 41 0 0 0 77 153 Z";
  const gate = "M118 26.4 C104 26.6 82 28.4 63 32 L65 37.5 L66 38 C56 50 42 62 33 71 C31 84 30.5 100 30.5 116 L31 126 L44 126 L44 100 C45 86 50 72 60 58 L76 38 C84 33 98 30 116 28.6 Z";
  const opening = "M98 28 L66 38 C56 50 42 62 33 71 C31 84 30.5 100 30.5 116 L31 126 L44 126 L44 100 C45 86 50 72 60 58 L76 38 Z";
  return `<svg viewBox="-42 -8 520 208" class="car" preserveAspectRatio="xMidYMid meet" role="img" aria-label="${aria}">
<defs>
<linearGradient id="paint-${u}" gradientUnits="userSpaceOnUse" x1="0" y1="27" x2="0" y2="157">
<stop offset="0" stop-color="${p.hi}"></stop>
<stop offset="0.1" stop-color="${p.mid}"></stop>
<stop offset="0.4" stop-color="${p.mid}"></stop>
<stop offset="0.46" stop-color="${p.hz}"></stop>
<stop offset="0.53" stop-color="${p.bo}"></stop>
<stop offset="0.82" stop-color="${p.low}"></stop>
<stop offset="1" stop-color="${p.deep}"></stop>
</linearGradient>
<linearGradient id="sweep-${u}" gradientUnits="userSpaceOnUse" x1="30" y1="0" x2="460" y2="0">
<stop offset="0" stop-color="#ffffff" stop-opacity="0"></stop>
<stop offset="0.5" stop-color="#ffffff" stop-opacity="0"></stop>
<stop offset="0.58" stop-color="#ffffff" stop-opacity="0.2"></stop>
<stop offset="0.61" stop-color="#ffffff" stop-opacity="0.32"></stop>
<stop offset="0.66" stop-color="#ffffff" stop-opacity="0"></stop>
<stop offset="0.86" stop-color="#ffffff" stop-opacity="0"></stop>
<stop offset="0.92" stop-color="#ffffff" stop-opacity="0.14"></stop>
<stop offset="1" stop-color="#ffffff" stop-opacity="0"></stop>
</linearGradient>
<linearGradient id="sill-${u}" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#000000" stop-opacity="0"></stop>
<stop offset="1" stop-color="#000000" stop-opacity="0.4"></stop>
</linearGradient>
<linearGradient id="glass-${u}" gradientUnits="userSpaceOnUse" x1="0" y1="34" x2="0" y2="74">
<stop offset="0" stop-color="#7f8a96"></stop>
<stop offset="0.28" stop-color="#2a3139"></stop>
<stop offset="1" stop-color="#08090b"></stop>
</linearGradient>
<linearGradient id="chrome-${u}" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#7d858c"></stop>
<stop offset="0.5" stop-color="#f4f6f8"></stop>
<stop offset="1" stop-color="#8b9299"></stop>
</linearGradient>
<linearGradient id="spokeG-${u}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#f1f3f5"></stop>
<stop offset="1" stop-color="#868d94"></stop>
</linearGradient>
<radialGradient id="tire-${u}" cx="0.5" cy="0.5" r="0.5">
<stop offset="0.7" stop-color="#1c1d20"></stop>
<stop offset="0.9" stop-color="#27292c"></stop>
<stop offset="1" stop-color="#0b0b0c"></stop>
</radialGradient>
<linearGradient id="cargo-${u}" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#060708"></stop>
<stop offset="1" stop-color="#23272b"></stop>
</linearGradient>
<linearGradient id="tail-${u}" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="${tailHi}"></stop>
<stop offset="1" stop-color="${tailLo}"></stop>
</linearGradient>
<filter id="soft-${u}" x="-20%" y="-300%" width="140%" height="700%"><feGaussianBlur stdDeviation="4"></feGaussianBlur></filter>
<filter id="glow-${u}" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="7"></feGaussianBlur></filter>
<clipPath id="bc-${u}"><path d="${body}"></path></clipPath>
<clipPath id="gc-${u}"><path d="${dlo}"></path></clipPath>
<path id="sp-${u}" d="M-1.2 -7 L-3.6 -24.6 L-0.9 -24.9 L0.7 -7 Z M1.6 -6.8 L4.4 -24.5 L7.1 -23.8 L3.2 -6.2 Z" fill="url(#spokeG-${u})"></path>
<g id="wheel-${u}">
<circle r="34.5" fill="url(#tire-${u})"></circle>
<circle r="31.8" fill="none" stroke="#34373b" stroke-width="0.8"></circle>
<circle r="25.6" fill="#15171a"></circle>
<circle r="18" fill="#4e5359"></circle>
<use href="#sp-${u}"></use>
<use href="#sp-${u}" transform="rotate(72)"></use>
<use href="#sp-${u}" transform="rotate(144)"></use>
<use href="#sp-${u}" transform="rotate(216)"></use>
<use href="#sp-${u}" transform="rotate(288)"></use>
<circle r="25" fill="none" stroke="url(#chrome-${u})" stroke-width="1.6"></circle>
<circle r="7" fill="#2a2e33"></circle>
<circle r="3.4" fill="#b4bac0"></circle>
</g>
</defs>

<ellipse cx="245" cy="185" rx="228" ry="6" fill="#000000" opacity="0.75" filter="url(#soft-${u})"></ellipse>
<ellipse cx="249" cy="183" rx="140" ry="5" fill="#000000" opacity="0.55" filter="url(#soft-${u})"></ellipse>
<ellipse cx="118" cy="186" rx="30" ry="2.6" fill="#000000"></ellipse>
<ellipse cx="380" cy="186" rx="30" ry="2.6" fill="#000000"></ellipse>
<ellipse cx="470" cy="104" rx="34" ry="16" fill="#fff4c8" opacity="${beam}" filter="url(#glow-${u})"></ellipse>
<ellipse cx="22" cy="79" rx="20" ry="10" fill="#ff2a40" opacity="${tailGlow}" filter="url(#glow-${u})"></ellipse>

<circle cx="118" cy="152" r="41" fill="#060607"></circle>
<circle cx="380" cy="152" r="41" fill="#060607"></circle>


<path d="${body}" fill="url(#paint-${u})"></path>
<g clip-path="url(#bc-${u})">
<rect x="20" y="20" width="450" height="140" fill="url(#sweep-${u})"></rect>
<rect x="20" y="128" width="450" height="30" fill="url(#sill-${u})"></rect>
<path d="M337 131 C280 129 200 124 158 108 L150 156 L340 156 Z" fill="#000000" opacity="0.09"></path>
<path d="M30 74 L80 76 C200 80 320 84 440 90 L440 94 C320 88 200 84 80 81 L30 80 Z" fill="#000000" opacity="0.1"></path>
</g>
<path d="M428 89.5 C360 85.5 200 81 74 78.5" stroke="#ffffff" stroke-opacity="0.6" stroke-width="1.1" fill="none"></path>
<path d="M428 91.5 C360 87.5 200 83 74 80.5" stroke="#000000" stroke-opacity="0.22" stroke-width="1.2" fill="none"></path>
<path d="M158 108 C200 124 280 129 337 131" stroke="#ffffff" stroke-opacity="0.5" stroke-width="1" fill="none"></path>
<path d="M432 80.5 C410 76.5 372 73.5 344 72" stroke="#ffffff" stroke-opacity="0.55" stroke-width="1.1" fill="none"></path>
<path d="M134 27.6 L232 28 C250 28.5 262 30 273 33.6" stroke="#ffffff" stroke-opacity="0.4" stroke-width="1" fill="none"></path>
<path d="M332 128 A50 50 0 0 1 428 128" stroke="#ffffff" stroke-opacity="0.16" stroke-width="1.2" fill="none"></path>
<path d="M70 128 A50 50 0 0 1 166 128" stroke="#ffffff" stroke-opacity="0.16" stroke-width="1.2" fill="none"></path>

<path d="M343 71 C322 60 296 44 274 33 C262 29.5 250 28 232 27.5 L132 27 L98 28 L103 40 C106 37 112 35 122 34.5 L262 34 C272 34 280 35.5 286 39 C304 50 322 62 337 73.5 Z" fill="#101113" opacity="${roofO}"></path>

<path d="${dlo}" fill="url(#glass-${u})"></path>
<g clip-path="url(#gc-${u})">
<path d="M296 30 L314 30 L290 80 L272 80 Z" fill="#ffffff" opacity="0.12"></path>
<path d="M186 30 L196 30 L172 80 L162 80 Z" fill="#ffffff" opacity="0.08"></path>
<path d="M90 60 Q220 58 340 64 L340 80 L90 80 Z" fill="#000000" opacity="0.35"></path>
</g>
<path d="M221 34.2 L229 34.1 L229.5 72.3 L221.5 72.4 Z" fill="#0b0c0e"></path>
<path d="M131 34.6 L139 34.5 L138 70.6 L130 70 Z" fill="#0b0c0e"></path>
<path d="M106 60 L103 40 C106 36.5 112 35 122 34.5 L262 34 C272 34 280 35.5 286 39 C304 50 322 62 337 73.5" stroke="#0b0c0e" stroke-width="1.6" fill="none" stroke-linejoin="round"></path>
<path d="M338 74.8 L160 71.8 C135 71.3 120 68.3 105.5 61.3" stroke="url(#chrome-${u})" stroke-width="1.6" fill="none" stroke-linecap="round"></path>

<path d="M335 76 C335.5 100 336 130 337 152" stroke="#000000" stroke-opacity="0.45" stroke-width="1" fill="none"></path>
<path d="M225.5 73 L226.5 152" stroke="#000000" stroke-opacity="0.45" stroke-width="1" fill="none"></path>
<path d="M130 71 C131 86 136 98 146 106 C156 114 162 122 163 132" stroke="#000000" stroke-opacity="0.45" stroke-width="1" fill="none"></path>
<rect x="233" y="81.5" width="17" height="3.4" rx="1.7" fill="url(#chrome-${u})"></rect>
<rect x="137" y="79.5" width="17" height="3.4" rx="1.7" fill="url(#chrome-${u})"></rect>

<path d="M302 80 C300 73 302 66 308 63.5 L318 64.5 C321 68 321 75 318.5 79.5 Z" fill="url(#paint-${u})"></path>
<path d="M303 80 L318.5 79.5 L322 77 L328 79 L326 83 L306 83.5 Z" fill="#121315"></path>
<path d="M304 68 Q310 64 318 65" stroke="#ffffff" stroke-opacity="0.55" stroke-width="1" fill="none"></path>

<path d="M159 150.5 L339 150.5 L339 157.5 L159 157.5 Z" fill="#121315"></path>
<path d="M159 150.5 L339 150.5" stroke="#ffffff" stroke-opacity="0.12" stroke-width="1"></path>
<path d="M335 154 A45 45 0 0 1 425 154" stroke="#121315" stroke-width="8" fill="none"></path>
<path d="M73 154 A45 45 0 0 1 163 154" stroke="#121315" stroke-width="8" fill="none"></path>
<path d="M422 152 L451 155.5 C455.5 151 457.5 144 458.5 135 L426 137 Z" fill="#121315"></path>
<path d="M432 150 L452 147" stroke="#b8bec4" stroke-width="1.6" stroke-linecap="round"></path>
<path d="M77 152 L36.5 151.5 C33.5 147 32 141 31.5 134 L74 136.5 Z" fill="#121315"></path>
<rect x="33" y="139" width="9" height="2.8" rx="1.4" fill="#6a0c17"></rect>

<path d="M408 83.6 C426 84.5 442 87.5 452.5 93 L451.6 96.4 C441 91.6 425 88.5 408 87.4 Z" fill="${drl}"></path>
<path d="M455.6 99 C457.6 107 458.6 116 458.4 125" stroke="url(#chrome-${u})" stroke-width="2" fill="none" stroke-linecap="round"></path>
<rect x="437" y="98" width="14" height="22" rx="6" fill="#1b2025"></rect>
<rect x="437" y="98" width="14" height="22" rx="6" fill="none" stroke="url(#chrome-${u})" stroke-width="1.3"></rect>
<rect x="440.5" y="102" width="7" height="4.2" rx="2" fill="${lamp}"></rect>
<rect x="440.5" y="107.6" width="7" height="4.2" rx="2" fill="${lamp}"></rect>
<rect x="440.5" y="113.2" width="7" height="3.6" rx="1.8" fill="${lamp}" opacity="0.7"></rect>
<path d="M447 130 L458 129.5" stroke="#3a3f45" stroke-width="2.2"></path>

${open?`
<path d="${opening}" fill="url(#cargo-${u})"></path>
<path d="M44 112 L34 112" stroke="#30343a" stroke-width="1.5"></path>
<path d="M58 62 C50 76 46 92 47 110" stroke="#2c3136" stroke-width="3" fill="none"></path>
`:''}

<path d="M44 75 L70 76 C72.2 77.4 72.2 80.2 70 81.6 L44 83.6 Z" fill="url(#tail-${u})"></path>
<path d="M46 76.4 L68 77.2" stroke="#ffffff" stroke-opacity="0.35" stroke-width="0.8"></path>

<g transform="${gateT}">
<path d="${gate}" fill="url(#paint-${u})"></path>
<path d="M98 30 L66 37.6 C60 46 54 53 47.5 60.5 L55.5 60.5 C63 50 76 40 98 30 Z" fill="url(#glass-${u})"></path>
<path d="M65 37.5 C80 33 96 30 116 28.6" stroke="#121315" stroke-width="1.4" fill="none"></path>
<path d="M118 26.5 C104 26.7 82 28.5 63.2 32.1" stroke="#ffffff" stroke-opacity="0.5" stroke-width="0.9" fill="none"></path>
<path d="M33 73.5 L44 75 L44 83.6 L32 83 Z" fill="url(#tail-${u})"></path>
<path d="M31 126 L44 126 L44 100 C45 86 50 72 60 58 L76 38" stroke="#000000" stroke-opacity="0.45" stroke-width="1" fill="none"></path>
<path d="M33 106 L43 106" stroke="url(#chrome-${u})" stroke-width="1.5"></path>
</g>

<use href="#wheel-${u}" x="118" y="152"></use>
<use href="#wheel-${u}" x="380" y="152"></use>
</svg>`;
}

function cabinSvg({ front, rear, wheel, running, paint, u, aria }) {
  const p = PAINTS[paint] || PAINTS.blanc;
  const glow = (on) => (on ? 1 : 0);
  const seat = (x, y, w, h, back, head) =>
    '<g><rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="9" fill="url(#seat-' + u + ')"/>' +
    '<rect x="' + (x + 5) + '" y="' + (y + 6) + '" width="' + (w - 10) + '" height="' + (h - 14) + '" rx="6" fill="#ffffff" opacity=".05"/>' +
    '<path d="M' + (x + w / 2) + " " + (y + 8) + " V" + (y + h - 8) + '" stroke="#000" stroke-opacity=".25" stroke-width="1"/>' +
    '<rect x="' + (x - 1) + '" y="' + (y + h - 2) + '" width="' + (w + 2) + '" height="' + back + '" rx="6" fill="url(#back-' + u + ')"/>' +
    (head ? '<rect x="' + (x + w / 2 - 10) + '" y="' + (y + h + back - 4) + '" width="20" height="9" rx="4" fill="#3a3f46"/>' : "") + "</g>";
  const lines = (y0, x0, x1, n, curve) => {
    let d = "";
    for (let i = 0; i < n; i++) { const y = y0 + i * 5; d += "M" + x0 + " " + y + " Q120 " + (y + curve) + " " + x1 + " " + y + " "; }
    return d;
  };
  return '<svg class="cabin" viewBox="0 0 240 400" role="img" aria-label="' + aria + '"><defs>' +
    '<linearGradient id="tp-' + u + '" x1="0" x2="1"><stop offset="0" stop-color="' + p.low + '"/><stop offset=".22" stop-color="' + p.mid + '"/><stop offset=".5" stop-color="' + p.hi + '"/><stop offset=".78" stop-color="' + p.mid + '"/><stop offset="1" stop-color="' + p.low + '"/></linearGradient>' +
    '<linearGradient id="gl-' + u + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7d8995"/><stop offset=".5" stop-color="#2a323b"/><stop offset="1" stop-color="#11151a"/></linearGradient>' +
    '<linearGradient id="fl-' + u + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14171a"/><stop offset="1" stop-color="#1e2226"/></linearGradient>' +
    '<linearGradient id="seat-' + u + '" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#5a6068"/><stop offset="1" stop-color="#363b41"/></linearGradient>' +
    '<linearGradient id="back-' + u + '" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4b5158"/><stop offset="1" stop-color="#2c3035"/></linearGradient>' +
    '<radialGradient id="warm-' + u + '" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#ff8a3d" stop-opacity=".38"/><stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/></radialGradient>' +
    '<radialGradient id="heat-' + u + '"><stop offset="0" stop-color="#ff8a3d" stop-opacity=".9"/><stop offset="1" stop-color="#ff8a3d" stop-opacity="0"/></radialGradient>' +
    '<filter id="blur-' + u + '" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>' +
    "</defs>" +
    '<ellipse cx="120" cy="206" rx="104" ry="196" fill="#000" opacity=".55" filter="url(#blur-' + u + ')"/>' +
    '<ellipse cx="32" cy="124" rx="11" ry="7" fill="url(#tp-' + u + ')"/><ellipse cx="208" cy="124" rx="11" ry="7" fill="url(#tp-' + u + ')"/>' +
    '<path d="M120 8 C170 8 196 22 200 60 L204 140 C206 200 206 300 202 350 C198 384 170 394 120 394 C70 394 42 384 38 350 C34 300 34 200 36 140 L40 60 C44 22 70 8 120 8 Z" fill="url(#tp-' + u + ')" stroke="#00000055" stroke-width="1"/>' +
    '<path d="M84 22 Q120 16 156 22 M70 40 Q78 70 74 96 M170 40 Q162 70 166 96" stroke="#000" stroke-opacity=".12" stroke-width="1.2" fill="none"/>' +
    '<path d="M48 22 Q58 12 76 12 L66 26 Z M192 22 Q182 12 164 12 L174 26 Z" fill="' + (running ? "#ffffff" : "#d9e2ea") + '"/>' +
    '<path d="M46 384 Q58 392 78 392 L74 384 Z M194 384 Q182 392 162 392 L166 384 Z" fill="#c0182c"/>' +
    '<path d="M54 102 Q120 86 186 102 L178 140 Q120 130 62 140 Z" fill="url(#gl-' + u + ')"/>' +
    '<path d="M70 108 L96 98 L90 134 L66 138 Z" fill="#fff" opacity=".1"/>' +
    '<path d="' + lines(106, 66, 174, 5, -6) + '" stroke="#ff9a5a" stroke-width="1.6" fill="none" opacity="' + glow(front) + '"/>' +
    '<rect x="52" y="140" width="136" height="196" rx="16" fill="url(#fl-' + u + ')"/>' +
    '<rect x="52" y="140" width="136" height="196" rx="16" fill="url(#warm-' + u + ')" opacity="' + glow(running) + '"/>' +
    '<path d="M52 150 Q52 140 64 140 L176 140 Q188 140 188 150 L188 166 Q120 156 52 166 Z" fill="#2a2e33"/>' +
    '<rect x="100" y="146" width="40" height="9" rx="2" fill="#0f1a26" stroke="#3b5672" stroke-width=".8"/>' +
    '<path d="M60 160 Q72 156 82 160 M158 160 Q168 156 180 160" stroke="#6b737c" stroke-width="2" stroke-linecap="round" fill="none"/>' +
    '<ellipse cx="86" cy="174" rx="24" ry="12" fill="url(#heat-' + u + ')" opacity="' + glow(wheel) + '"/>' +
    '<ellipse cx="86" cy="174" rx="17" ry="6.5" fill="none" stroke="' + (wheel ? "#ffa063" : "#8a9199") + '" stroke-width="3.5"/>' +
    '<path d="M70 174 H102 M86 174 V180" stroke="' + (wheel ? "#ffa063" : "#8a9199") + '" stroke-width="2.2"/><circle cx="86" cy="174" r="3.5" fill="#2a2e33"/>' +
    '<rect x="110" y="164" width="20" height="96" rx="7" fill="#26292d" stroke="#33373c" stroke-width="1"/>' +
    '<circle cx="120" cy="184" r="4.5" fill="#4a5058"/><circle cx="115" cy="206" r="4" fill="#15181b"/><circle cx="125" cy="206" r="4" fill="#15181b"/>' +
    seat(62, 186, 42, 44, 18, true) + seat(136, 186, 42, 44, 18, true) +
    '<rect x="56" y="268" width="128" height="4" rx="2" fill="#000" opacity=".3"/>' +
    seat(58, 274, 40, 36, 14, true) + seat(100, 274, 40, 36, 14, true) + seat(142, 274, 40, 36, 14, true) +
    '<path d="M44 160 L46 320 M196 160 L194 320" stroke="#000" stroke-opacity=".15" stroke-width="1"/>' +
    '<path d="M62 342 Q120 350 178 342 L184 362 Q120 372 56 362 Z" fill="url(#gl-' + u + ')"/>' +
    '<path d="' + lines(348, 66, 174, 3, 4) + '" stroke="#ff9a5a" stroke-width="1.4" fill="none" opacity="' + glow(rear) + '"/>' +
    "</svg>";
}

const CSS = String.raw`
:host{display:block;height:100%}
ha-card{position:relative;overflow:hidden;height:100%;box-sizing:border-box;padding:18px 16px 16px;border-radius:var(--ha-card-border-radius,24px);
background:var(--mitsubishi-card-background,linear-gradient(180deg,#33383e 0%,#1a1c1f 42%,#0e0f11 100%));color:var(--mitsubishi-card-text,#f2f3f4);
display:flex;flex-direction:column;gap:12px;font-family:inherit}
button{font:inherit;color:inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}
button:focus-visible{outline:2px solid var(--primary-color,#5b8cff);outline-offset:2px}
button:disabled{cursor:default;opacity:.45}
.muted{color:var(--mitsubishi-card-muted,#a7adb4)}
.head{display:flex;align-items:flex-start;gap:12px}
.ttl{flex:1;min-width:0}
.name{font-size:26px;font-weight:500;letter-spacing:-.02em;line-height:1.1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sub{font-size:13px;margin-top:4px}
.rng{text-align:right;white-space:nowrap}
.rng b{display:block;font-size:20px;font-weight:500}
.rng span{font-size:13px}
.gauge{display:inline-block;vertical-align:middle;width:30px;height:13px;border:1.5px solid #c9ced3;border-radius:4px;box-sizing:border-box;padding:1.5px;margin-left:6px}
.gauge i{display:block;height:100%;border-radius:1.5px;background:currentColor}
.stage{position:relative;margin:0 -6px}
.stage svg.car{display:block;width:100%;height:auto;aspect-ratio:500/200}
.stage img{display:block;width:100%;height:auto}
.chip{position:absolute;top:2px;left:26%;display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px;border-radius:13px;background:rgba(20,22,25,.8);color:#ffd28a;font-size:13px;white-space:nowrap}
.chip i{width:7px;height:7px;border-radius:4px;background:#ffb547}
.acts{display:grid;grid-template-columns:repeat(var(--n,5),minmax(0,1fr));gap:4px}
.act{border:0;background:transparent;padding:0;display:flex;flex-direction:column;align-items:center;gap:6px;font-size:12px;line-height:1.2;text-align:center}
.act .o{width:52px;height:52px;border-radius:26px;display:flex;align-items:center;justify-content:center;background:#2c3035;box-shadow:inset 0 1px 0 rgba(255,255,255,.12);transition:background .2s}
.act.on .o{background:#f2f3f4;color:#111214}
.act.blue .o{background:var(--mitsubishi-accent,#5b8cff);color:#0b1530}
.act.warm .o{background:#ff7a2e;color:#2a1206}
.act.busy .o{animation:pulse 1.1s ease-in-out infinite}
@keyframes pulse{50%{opacity:.45}}
@media (prefers-reduced-motion:reduce){.act.busy .o{animation:none}}
.rows{display:flex;flex-direction:column;border-top:1px solid rgba(255,255,255,.08)}
.row{display:flex;align-items:center;gap:14px;min-height:56px;border:0;border-bottom:1px solid rgba(255,255,255,.08);background:transparent;padding:0;text-align:left;width:100%}
.row:last-child{border-bottom:0}
.row ha-icon{color:#a7adb4;--mdc-icon-size:22px;flex:none}
.row .t{flex:1;min-width:0}
.row .t b{display:block;font-size:15px;font-weight:400}
.row .t span{display:block;font-size:13px;color:#a7adb4;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.row .end{font-size:13px;white-space:nowrap}
.warn{color:#ffd28a}
.alert ha-icon,.alert .t b{color:#ff8a7a}
.pill{height:34px;padding:0 14px;border:0;border-radius:17px;background:#2c3035;font-size:13px;font-weight:500;white-space:nowrap}
.pill.on{background:#4cd18a;color:#06210f}
.status{min-height:36px;display:flex;align-items:center;gap:10px;padding:0 12px;border-radius:12px;font-size:13px;background:rgba(255,255,255,.05);color:#b9bec4}
.status.busy{background:rgba(91,140,255,.14);color:#cdd9ff}
.status.err{background:rgba(255,90,90,.14);color:#ffc2bb}
.status.ok{background:rgba(76,209,138,.12);color:#bdf0d2}
.dot{width:8px;height:8px;border-radius:4px;background:currentColor;flex:none}
.sheet{position:absolute;inset:0;background:rgba(6,7,8,.78);display:flex;align-items:center;justify-content:center;padding:16px;z-index:2}
.dlg{width:100%;max-width:320px;box-sizing:border-box;background:#1f2124;border-radius:24px;padding:20px;display:flex;flex-direction:column;gap:12px;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.dlg h3{margin:0;font-size:19px;font-weight:500}
.dlg p{margin:0;font-size:14px;color:#a7adb4}
.dlg .btns{display:flex;gap:8px;justify-content:flex-end;margin-top:4px}
.dlg .btns button{height:44px;padding:0 18px;border:0;border-radius:22px;background:transparent;color:#9db8ff;font-size:15px}
.dlg .btns .primary{background:#f2f3f4;color:#111214;font-weight:500}
.hold{position:relative;overflow:hidden;touch-action:none;user-select:none;-webkit-user-select:none}
.hold .fill{position:absolute;inset:0;transform:scaleX(0);transform-origin:left;background:#5b8cff}
.hold.holding .fill{transform:scaleX(1);transition:transform 1.5s linear}
.hold .l{position:relative}
.temp{display:flex;align-items:center;justify-content:center;gap:16px}
.temp button{width:52px;height:52px;border-radius:26px;border:0;background:#2c3035}
.temp .v{font-size:56px;font-weight:300;line-height:1;letter-spacing:-.03em;min-width:4ch;text-align:center;white-space:nowrap}
.temp .v small{font-size:26px}
.big{height:54px;border:0;border-radius:27px;background:#f2f3f4;color:#111214;font-size:16px;font-weight:500}
.big.stop{background:#2c3035;color:#f2f3f4}
.cabin{display:block;width:52%;max-width:200px;margin:0 auto;height:auto}
.empty{padding:24px 8px;text-align:center;color:#a7adb4}
.tile .stage{margin:-6px -4px -4px;flex:1 1 0;min-height:0;display:flex;align-items:center;justify-content:center}
.tile .stage svg.car,.tile .stage img{width:auto;max-width:100%;height:100%;object-fit:contain}
.tile .name{font-size:20px}
.tile .acts .o{width:44px;height:44px;border-radius:22px}
`;

class MitsubishiBaseCard extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this._u = "mc" + ++uidSeq;
    this._pending = null;
    this._msg = null;
    this._confirm = null;
    this._flashUntil = 0;
    this._sig = "";
    this.shadowRoot.addEventListener("click", (ev) => this._onClick(ev));
    const start = (ev) => {
      const el = ev.target.closest && ev.target.closest("[data-hold]");
      if (!el || this._holdTimer) return;
      if (ev.type === "keydown" && ev.key !== "Enter" && ev.key !== " ") return;
      ev.preventDefault();
      el.classList.add("holding");
      this._holdTimer = setTimeout(() => {
        this._holdTimer = null;
        if (this.isConnected && el.isConnected && this._confirm && this._confirm.hold) this._action(el.dataset.hold);
      }, 1500);
    };
    const stop = () => this._cancelHold();
    this.shadowRoot.addEventListener("pointerdown", start);
    this.shadowRoot.addEventListener("keydown", start);
    for (const type of ["pointerup", "pointercancel", "pointerleave", "keyup"]) this.shadowRoot.addEventListener(type, stop, true);
  }

  _cancelHold() {
    if (!this._holdTimer) return;
    clearTimeout(this._holdTimer);
    this._holdTimer = null;
    this.shadowRoot.querySelectorAll(".holding").forEach((n) => n.classList.remove("holding"));
  }

  disconnectedCallback() {
    this._cancelHold();
  }

  _render() {
    this._cancelHold();
    this._draw();
  }

  setConfig(config) {
    if (!config || typeof config !== "object") throw new Error("Invalid configuration");
    this._config = { confirm: true, paint: "blanc", ...config };
    this._sig = "";
    this._map = this._hass ? this._resolve() : null;
    if (this._hass) this._render();
  }

  set hass(hass) {
    const prevEntities = this._hass && this._hass.entities;
    this._hass = hass;
    if (!this._map || prevEntities !== hass.entities) this._map = this._resolve();
    const sig = this._signature();
    if (sig !== this._sig) {
      this._sig = sig;
      this._render();
    }
  }

  get t() {
    const lang = (this._hass && (this._hass.locale?.language || this._hass.language)) || "en";
    return TEXT[lang.slice(0, 2)] || TEXT.en;
  }

  _deviceId() {
    if (this._config.device) return this._config.device;
    const reg = this._hass.entities || {};
    const hit = Object.values(reg).find((e) => e.platform === DOMAIN && e.device_id);
    return hit ? hit.device_id : null;
  }

  _resolve() {
    const hass = this._hass;
    const overrides = this._config.entities || {};
    const reg = hass.entities || {};
    const device = this._deviceId();
    const own = Object.values(reg).filter((e) => device && e.device_id === device);
    const pool = own.length ? own.map((e) => e.entity_id) : Object.keys(hass.states);
    const map = { device };
    for (const [role, def] of Object.entries(ROLES)) {
      if (overrides[role]) { map[role] = overrides[role]; continue; }
      const byKey = own.find((e) => e.translation_key === def.key && e.entity_id.startsWith(def.domain + "."));
      if (byKey) { map[role] = byKey.entity_id; continue; }
      for (const sfx of def.suffixes) {
        const id = pool.find((x) => x.startsWith(def.domain + ".") && x.endsWith("_" + sfx) && (own.length || x.includes("mitsubishi")));
        if (id) { map[role] = id; break; }
      }
    }
    map.windows = pool.filter((id) => id.startsWith("binary_sensor.") && hass.states[id]?.attributes?.device_class === "window" && (own.length || id.includes("mitsubishi")));
    return map;
  }

  _st(role) {
    const id = this._map && this._map[role];
    return id ? this._hass.states[id] : undefined;
  }

  _on(role) { return this._st(role)?.state === "on"; }

  _fmt(role) {
    const s = this._st(role);
    if (!s || s.state === "unknown" || s.state === "unavailable") return null;
    if ((role === "range" || role === "odometer" || role === "ev_range") && !isNaN(Number(s.state))) {
      const unit = s.attributes.unit_of_measurement;
      return Math.round(Number(s.state)).toLocaleString(this._hass.locale?.language) + (unit ? " " + unit : "");
    }
    if (this._hass.formatEntityState) return this._hass.formatEntityState(s);
    const unit = s.attributes.unit_of_measurement;
    return unit ? s.state + " " + unit : s.state;
  }

  _signature() {
    const parts = [];
    for (const role of Object.keys(ROLES)) {
      const s = this._st(role);
      parts.push(s ? s.state + "|" + s.last_updated : "-");
    }
    for (const id of (this._map && this._map.windows) || []) parts.push(this._hass.states[id]?.state);
    parts.push(this._hass.locale?.language);
    return parts.join(";");
  }

  _ago(role) {
    const s = this._st(role);
    if (!s || !s.state || s.state === "unknown" || s.state === "unavailable") return this.t.never;
    const ms = Date.parse(s.state);
    if (Number.isNaN(ms)) return this.t.never;
    const mins = Math.round((ms - Date.now()) / 60000);
    const rtf = new Intl.RelativeTimeFormat(this._hass.locale?.language || "en", { numeric: "auto" });
    if (Math.abs(mins) < 60) return rtf.format(mins, "minute");
    const hours = Math.round(mins / 60);
    if (Math.abs(hours) < 48) return rtf.format(hours, "hour");
    return rtf.format(Math.round(hours / 24), "day");
  }

  _name() {
    if (this._config.name) return this._config.name;
    const dev = this._map.device && this._hass.devices ? this._hass.devices[this._map.device] : null;
    const name = (dev && (dev.name_by_user || dev.name)) || "Mitsubishi";
    return dev && dev.name_by_user ? name : name.replace(/^Mitsubishi\s+/i, "");
  }

  _car(open) {
    const c = this._config;
    if (c.image) {
      const src = open && c.image_trunk_open ? c.image_trunk_open : c.image;
      return '<img src="' + esc(src) + '" alt="">';
    }
    const lit = this._on("headlights") || Date.now() < this._flashUntil;
    return carSvg({ paint: c.paint, roofBlack: !!c.roof_black, open, lit, aria: esc(this._name()), u: this._u });
  }

  async _run(key, domain, service, role, data = {}) {
    const id = this._map[role];
    if (!id || this._pending) return;
    this._pending = key;
    this._msg = { kind: "busy", text: this.t.sending };
    this._render();
    try {
      await this._hass.callService(domain, service, { entity_id: id, ...data });
      if (key === "lights") {
        this._flashUntil = Date.now() + 2500;
        setTimeout(() => this._render(), 2600);
      }
      this._msg = { kind: "ok", text: this.t.pressed[key] || this.t.done };
    } catch (err) {
      this._msg = { kind: "err", text: this.t.failed + this.t.sep + ((err && err.message) || err) };
    } finally {
      this._pending = null;
      this._render();
      const shown = this._msg;
      setTimeout(() => { if (this._msg === shown) { this._msg = null; this._render(); } }, shown && shown.kind === "err" ? 9000 : 4000);
    }
  }

  _action(act) {
    const t = this.t;
    switch (act) {
      case "lock": return this._run("lock", "button", "press", "lock");
      case "unlock": return this._ask(act, t.confirmUnlock, t.confirmUnlockText);
      case "lights": return this._run("lights", "button", "press", "lights");
      case "horn": return this._run("horn", "button", "press", "horn");
      case "refresh": return this._run("refresh", "button", "press", "refresh");
      case "locate": return this._run("locate", "button", "press", "locate");
      case "engine":
        if (this._on("engine")) return this._run("engine_off", "button", "press", "stop_engine");
        {
          const o = this._openings();
          const text = o.open.length ? o.open.join(", ") + " " + t.open + t.sep + t.blocked + ". " + t.confirmStartText : t.confirmStartText;
          this._confirm = { act: "engine_on", title: t.confirmStart, text, hold: true };
        }
        return this._render();
      case "charging":
        return this._run(this._on("charging") ? "charging_off" : "charging_on", "switch", this._on("charging") ? "turn_off" : "turn_on", "charging");
      case "front_defrost": case "rear_defrost": case "steering_heater":
        return this._hass.callService("switch", "toggle", { entity_id: this._map[act] });
      case "temp_down": case "temp_up": return this._stepTemp(act === "temp_up" ? 1 : -1);
      case "more_tracker": return this._more("tracker");
      case "more_climate":
        if (this._config.climate_path) {
          history.pushState(null, "", this._config.climate_path);
          window.dispatchEvent(new CustomEvent("location-changed"));
          return;
        }
        return this._more("temperature");
      case "confirm_yes": {
        const c = this._confirm;
        this._confirm = null;
        if (c.act === "unlock") return this._run("unlock", "button", "press", "unlock");
        if (c.act === "engine_on") return this._run("engine_on", "button", "press", "start_engine");
        return this._render();
      }
      case "confirm_no": this._confirm = null; return this._render();
    }
  }

  _ask(act, title, text) {
    if (!this._config.confirm) {
      this._confirm = { act };
      return this._action("confirm_yes");
    }
    this._confirm = { act, title, text };
    this._render();
  }

  _stepTemp(dir) {
    const s = this._st("temperature");
    if (!s) return;
    const a = s.attributes;
    const step = Number(a.step) || 0.5;
    const v = Math.min(Number(a.max ?? 30), Math.max(Number(a.min ?? 16), Number(s.state) + dir * step));
    this._hass.callService("number", "set_value", { entity_id: this._map.temperature, value: v });
  }

  _more(role) {
    const id = this._map[role];
    if (!id) return;
    this.dispatchEvent(new CustomEvent("hass-more-info", { detail: { entityId: id }, bubbles: true, composed: true }));
  }

  _onClick(ev) {
    const el = ev.target.closest("[data-act]");
    if (!el || el.disabled) return;
    this._action(el.dataset.act);
  }

  _btn(act, icon, label, cls = "", role) {
    const missing = role && !this._map[role];
    if (missing) return "";
    const busy = this._pending && (this._pending === act || this._pending.startsWith(act + "_")) ? " busy" : "";
    return '<button class="act ' + cls + busy + '" data-act="' + act + '"' + (this._pending ? " disabled" : "") + ' aria-label="' + esc(label) + '"><span class="o"><ha-icon icon="' + icon + '"></ha-icon></span>' + esc(label) + "</button>";
  }

  _status() {
    if (!this._msg) return "";
    return '<div class="status ' + this._msg.kind + '" role="status"><span class="dot"></span><span>' + esc(this._msg.text) + "</span></div>";
  }

  _sheet() {
    if (!this._confirm || !this._confirm.title) return "";
    const t = this.t;
    return '<div class="sheet"><div class="dlg" role="dialog" aria-modal="true" aria-label="' + esc(this._confirm.title) + '"><h3>' + esc(this._confirm.title) + "</h3><p>" + esc(this._confirm.text) + '</p><div class="btns"><button data-act="confirm_no">' + esc(t.cancel) + "</button>" + (this._confirm.hold ? '<button class="primary hold" data-hold="confirm_yes"><span class="fill"></span><span class="l">' + esc(t.holdToStart) + "</span></button>" : '<button class="primary" data-act="confirm_yes">' + esc(t.confirm) + "</button>") + "</div></div></div>";
  }

  _openings() {
    const t = this.t;
    const open = OPENINGS.filter((r) => this._on(r)).map((r) => t[r]);
    const known = OPENINGS.some((r) => { const s = this._st(r); return s && s.state !== "unknown" && s.state !== "unavailable"; });
    const win = (this._map.windows || []).filter((id) => this._hass.states[id]?.state === "on").length;
    return { open, known, win };
  }

  _energy() {
    const t = this.t;
    const battery = this._st("battery");
    if (battery && !isNaN(Number(battery.state))) {
      const ev = this._fmt("ev_range");
      return { main: ev ? ev + " " + t.evRange : battery.state + " %", sub: t.battery + " " + battery.state + " %", pct: Number(battery.state) };
    }
    const fuel = this._st("fuel_level");
    const pct = fuel && !isNaN(Number(fuel.state)) ? Number(fuel.state) : null;
    return { main: this._fmt("range") || "", sub: pct != null ? pct + " %" : "", pct };
  }

  _emptyCard() {
    this.shadowRoot.innerHTML = "<style>" + CSS + '</style><ha-card><div class="empty">' + esc(this.t.noDevice) + "</div></ha-card>";
  }
}

class MitsubishiVehicleCard extends MitsubishiBaseCard {
  static getStubConfig() { return { paint: "blanc" }; }
  static getConfigForm() { return configForm(true); }
  getCardSize() { return 15; }
  getGridOptions() { return { columns: 12, rows: "auto", min_columns: 12 }; }

  _draw() {
    if (!this._hass || !this._config) return;
    if (!this._map.start_engine && !this._map.lock) return this._emptyCard();
    const t = this.t;
    const engineOn = this._on("engine");
    const o = this._openings();
    const trunkOpen = this._on("trunk");
    const e = this._energy();
    const gauge = e.pct != null ? '<span class="gauge"><i style="width:' + Math.max(0, Math.min(100, e.pct)) + '%"></i></span>' : "";
    const sub = (engineOn ? t.running : t.parked) + " · " + t.updated + " " + this._ago("updated");
    const chip = o.open.length ? '<span class="chip"><i></i>' + esc(o.open.join(", ") + " " + t.open) + "</span>" : "";

    const acts = [
      this._btn("lock", "mdi:car-door-lock", t.lock, "", "lock"),
      this._btn("unlock", "mdi:car-door-lock-open", t.unlock, "", "unlock"),
      this._btn("engine", "mdi:power", engineOn ? t.stop : t.start, engineOn ? "blue" : "", engineOn ? "stop_engine" : "start_engine"),
      this._btn("lights", "mdi:car-light-high", t.lights, Date.now() < this._flashUntil ? "on" : "", "lights"),
      this._btn("horn", "mdi:bullhorn-outline", t.horn, "", "horn"),
    ].filter(Boolean);

    const rows = [];
    const temp = this._fmt("temperature");
    const presets = ["front_defrost", "rear_defrost", "steering_heater"].filter((r) => this._on(r)).map((r) => t[r]);
    if (this._map.temperature || this._map.start_engine) {
      const line = (engineOn ? t.running : t.target + " " + (temp || "")) + (presets.length ? " · " + presets.join(", ") : "");
      rows.push(this._row("more_climate", "mdi:thermometer", t.climate, line, '<ha-icon icon="mdi:chevron-right"></ha-icon>'));
    }
    if (this._map.charging) {
      const on = this._on("charging");
      rows.push('<div class="row"><ha-icon icon="mdi:ev-station"></ha-icon><span class="t"><b>' + esc(t.charging) + "</b><span>" + esc(this._fmt("battery") || "") + '</span></span><button class="pill' + (on ? " on" : "") + '" data-act="charging"' + (this._pending ? " disabled" : "") + ">" + esc(on ? t.stop : t.charge) + "</button></div>");
    }
    if (this._map.tracker) {
      const tr = this._st("tracker");
      const loc = this._fmt("tracker") || t.unknown;
      const when = tr && tr.attributes.latitude != null ? tr.attributes.latitude.toFixed(4) + ", " + tr.attributes.longitude.toFixed(4) : "";
      rows.push('<div class="row"><button class="row" style="border:0;min-height:0;flex:1" data-act="more_tracker"><ha-icon icon="mdi:map-marker-outline"></ha-icon><span class="t"><b>' + esc(t.location) + "</b><span>" + esc(loc + (when ? " · " + when : "")) + "</span></span></button>" + (this._map.locate ? '<button class="pill" data-act="locate" aria-label="' + esc(t.locate) + '"' + (this._pending ? " disabled" : "") + '><ha-icon icon="mdi:crosshairs-gps" style="--mdc-icon-size:18px"></ha-icon></button>' : "") + "</div>");
    }
    const openText = !o.known ? t.unknown : o.open.length ? o.open.join(", ") + " " + t.open : t.allClosed;
    const winText = o.win ? " · " + o.win + " " + t.windowsOpen : "";
    rows.push('<div class="row"><ha-icon icon="mdi:car-door"></ha-icon><span class="t"><b>' + esc(t.openings) + '</b><span class="' + (o.open.length || o.win ? "warn" : "") + '">' + esc(openText + winText) + "</span></span></div>");
    const warns = ["brake_warning", "oil_warning"].filter((r) => this._on(r)).map((r) => t[r]);
    if (warns.length) rows.push('<div class="row alert"><ha-icon icon="mdi:alert-outline"></ha-icon><span class="t"><b>' + esc(t.warnings) + "</b><span>" + esc(warns.join(", ")) + "</span></span></div>");
    if (this._map.odometer || this._map.refresh) {
      rows.push(this._row("refresh", "mdi:counter", t.odometer + " " + (this._fmt("odometer") || ""), t.updated + " " + this._ago("updated"), '<ha-icon icon="mdi:refresh"></ha-icon>', !this._map.refresh));
    }

    this.shadowRoot.innerHTML = "<style>" + CSS + "</style><ha-card>" +
      '<div class="head"><div class="ttl"><div class="name">' + esc(this._name()) + '</div><div class="sub muted">' + esc(sub) + '</div></div><div class="rng"><b>' + esc(e.main) + gauge + '</b><span class="muted">' + esc(e.sub) + "</span></div></div>" +
      '<div class="stage">' + this._car(trunkOpen) + chip + "</div>" +
      '<div class="acts" style="--n:' + acts.length + '">' + acts.join("") + "</div>" +
      '<div class="rows">' + rows.join("") + "</div>" + this._status() + this._sheet() + "</ha-card>";
  }

  _row(act, icon, title, line, end, disabled) {
    return '<button class="row" data-act="' + act + '"' + (disabled || (act === "refresh" && this._pending) ? " disabled" : "") + '><ha-icon icon="' + icon + '"></ha-icon><span class="t"><b>' + esc(title) + "</b><span>" + esc(line) + '</span></span><span class="end muted">' + end + "</span></button>";
  }
}

class MitsubishiClimateCard extends MitsubishiBaseCard {
  static getStubConfig() { return {}; }
  static getConfigForm() { return configForm(false); }
  getCardSize() { return 10; }
  getGridOptions() { return { columns: 12, rows: "auto", min_columns: 6 }; }

  _draw() {
    if (!this._hass || !this._config) return;
    if (!this._map.start_engine && !this._map.temperature) return this._emptyCard();
    const t = this.t;
    const engineOn = this._on("engine");
    const s = this._st("temperature");
    const unit = s ? s.attributes.unit_of_measurement || "°C" : "°C";
    const val = s && !isNaN(Number(s.state)) ? Number(s.state).toLocaleString(this._hass.locale?.language, { maximumFractionDigits: 1 }) : "--";
    const front = this._on("front_defrost"), rear = this._on("rear_defrost"), wheel = this._on("steering_heater");
    const cabin = cabinSvg({ front, rear, wheel, running: engineOn, paint: this._config.paint, u: this._u, aria: esc(t.climate) });
    const toggles = ["front_defrost", "rear_defrost", "steering_heater"].map((r) => this._map[r] ? this._btn(r, r === "steering_heater" ? "mdi:steering" : r === "front_defrost" ? "mdi:car-defrost-front" : "mdi:car-defrost-rear", t[r], this._on(r) ? "warm" : "") : "").filter(Boolean);
    const cur = engineOn && this._fmt("cabin_target") ? '<div class="muted" style="text-align:center;font-size:13px">' + esc(t.target + " " + this._fmt("cabin_target")) + "</div>" : "";
    this.shadowRoot.innerHTML = "<style>" + CSS + "</style><ha-card>" +
      '<div class="head"><div class="ttl"><div class="name">' + esc(t.climate) + '</div><div class="sub muted">' + esc(engineOn ? t.running : t.presetsNote) + "</div></div></div>" + cabin +
      (s ? '<div class="temp"><button data-act="temp_down" aria-label="-"><ha-icon icon="mdi:chevron-left"></ha-icon></button><div class="v">' + esc(val) + "<small>" + esc(unit) + '</small></div><button data-act="temp_up" aria-label="+"><ha-icon icon="mdi:chevron-right"></ha-icon></button></div>' : "") + cur +
      (toggles.length ? '<div class="acts" style="--n:' + toggles.length + '">' + toggles.join("") + "</div>" : "") +
      this._status() +
      (this._map.start_engine ? '<button class="big' + (engineOn ? " stop" : "") + '" data-act="engine"' + (this._pending ? " disabled" : "") + ">" + esc(engineOn ? t.stopEngine : t.startWith) + "</button>" : "") +
      this._sheet() + "</ha-card>";
  }
}

class MitsubishiVehicleTile extends MitsubishiBaseCard {
  static getStubConfig() { return { paint: "blanc" }; }
  static getConfigForm() { return configForm(true); }
  getCardSize() { return 5; }
  getGridOptions() { return { columns: 12, rows: 4, min_rows: 4, min_columns: 6 }; }

  _draw() {
    if (!this._hass || !this._config) return;
    if (!this._map.start_engine && !this._map.lock) return this._emptyCard();
    const t = this.t;
    const engineOn = this._on("engine");
    const o = this._openings();
    const e = this._energy();
    const line = this._msg ? this._msg.text : (engineOn ? t.running : t.parked) + (o.open.length ? " · " + o.open.join(", ") + " " + t.open : "");
    const acts = [
      this._btn("lock", "mdi:car-door-lock", t.lock, "", "lock"),
      this._btn("unlock", "mdi:car-door-lock-open", t.unlock, "", "unlock"),
      this._btn("engine", "mdi:power", engineOn ? t.stop : t.start, engineOn ? "blue" : "", engineOn ? "stop_engine" : "start_engine"),
      this._btn("lights", "mdi:car-light-high", t.lights, "", "lights"),
    ].filter(Boolean);
    this.shadowRoot.innerHTML = "<style>" + CSS + '</style><ha-card class="tile" style="gap:6px;padding:14px 14px 12px">' +
      '<div class="head"><div class="ttl"><div class="name">' + esc(this._name()) + '</div><div class="sub ' + (this._msg && this._msg.kind === "err" ? "warn" : "muted") + '">' + esc(line) + '</div></div><div class="rng"><b>' + esc(e.main) + "</b></div></div>" +
      '<div class="stage">' + this._car(this._on("trunk")) + "</div>" +
      '<div class="acts" style="--n:' + acts.length + '">' + acts.join("") + "</div>" + this._sheet() + "</ha-card>";
  }
}

function configForm(withLook) {
  const schema = [
    { name: "device", selector: { device: { filter: { integration: DOMAIN } } } },
    { name: "name", selector: { text: {} } },
  ];
  if (withLook) {
    schema.push(
      { name: "paint", selector: { select: { mode: "dropdown", options: Object.keys(PAINTS) } } },
      { name: "roof_black", selector: { boolean: {} } },
      { name: "image", selector: { text: {} } },
      { name: "image_trunk_open", selector: { text: {} } },
    );
  }
  schema.push({ name: "confirm", selector: { boolean: {} } });
  const labels = { device: "Vehicle", name: "Name", paint: "Paint", roof_black: "Black roof", image: "Image URL (/local/...)", image_trunk_open: "Image URL, tailgate open", confirm: "Confirm unlock (remote start always needs a 1.5 s hold)" };
  return { schema, computeLabel: (s) => labels[s.name] || s.name };
}

const CARDS = [
  ["mitsubishi-vehicle-card", MitsubishiVehicleCard, "Mitsubishi vehicle", "Vehicle render, remote commands, openings, location and odometer."],
  ["mitsubishi-climate-card", MitsubishiClimateCard, "Mitsubishi climate", "Remote start temperature, defrost and heated wheel presets, engine start."],
  ["mitsubishi-vehicle-tile", MitsubishiVehicleTile, "Mitsubishi vehicle tile", "Compact vehicle tile with quick commands."],
];
window.customCards = window.customCards || [];
for (const [tag, cls, name, description] of CARDS) {
  if (!customElements.get(tag)) customElements.define(tag, cls);
  if (!window.customCards.some((c) => c.type === tag)) window.customCards.push({ type: tag, name, description, preview: true, documentationURL: "https://github.com/damione1/mitsubishi-connect-ha" });
}

;(function (global) {
  const DEFAULT_CABLE_TYPES = {
    power: { label: 'Power', maxLength_mm: 3048, color: '#1f2933' },
    air: { label: 'Compressed Air', maxLength_mm: 3048, color: '#e5e7eb' },
    n2: { label: 'Nitrogen', maxLength_mm: 3048, color: '#16a34a' },
    ground: { label: 'Ground', maxLength_mm: 3048, color: '#22c55e' },
    vacuum: { label: 'Vacuum', maxLength_mm: 3048, color: 'rgba(255,255,255,0.7)' },
    water: { label: 'Water', maxLength_mm: 3048, color: '#1d4ed8' },
    ethernet: { label: 'Ethernet', maxLength_mm: 3048, color: '#facc15' }
  };

  const ALL_CABLE_TYPES = Object.keys(DEFAULT_CABLE_TYPES);

  const DEFAULT_ASSET_CATALOG = {
    microscope: {
      boundingBox_mm: { w: 2200, l: 1800, h: 2200 },
      connectionSockets: [
        {
          id: 'microscope_power',
          label: 'Microscope Power',
          anchor: { u: 0.1, v: 0.2, w: 0.1 },
          surface: 'floor',
          allowedCableTypes: ['power', 'ground']
        },
        {
          id: 'microscope_vacuum',
          label: 'Vacuum Input',
          anchor: { u: 0.9, v: 0.2, w: 0.1 },
          surface: 'floor',
          allowedCableTypes: ['vacuum']
        }
      ]
    },
    table: {
      boundingBox_mm: { w: 1800, l: 900, h: 900 },
      connectionSockets: [
        {
          id: 'table_power',
          label: 'Table Power',
          anchor: { u: 0.5, v: 0.5, w: 0.1 },
          surface: 'floor',
          allowedCableTypes: ['power', 'ground', 'ethernet']
        }
      ]
    },
    pump: {
      boundingBox_mm: { w: 1200, l: 600, h: 1200 },
      connectionSockets: [
        {
          id: 'pump_power',
          label: 'Pump Power',
          anchor: { u: 0.5, v: 0.5, w: 0.1 },
          surface: 'floor',
          allowedCableTypes: ['power', 'ground']
        },
        {
          id: 'pump_vacuum',
          label: 'Pump Vacuum',
          anchor: { u: 0.1, v: 0.5, w: 0.1 },
          surface: 'floor',
          allowedCableTypes: ['vacuum']
        }
      ]
    },
    floorBox: {
      boundingBox_mm: { w: 600, l: 600, h: 200 },
      connectionSockets: [
        {
          id: 'floor_box_power',
          label: 'Floor Box Power',
          anchor: { u: 0.5, v: 0.5, w: 0 },
          surface: 'floor',
          allowedCableTypes: ['power', 'ground', 'ethernet']
        }
      ]
    },
    wall_socket: {
      boundingBox_mm: { w: 400, l: 120, h: 600 },
      connectionSockets: [
        {
          id: 'wall_outlet_duplex',
          label: 'Duplex Outlet',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'wall',
          allowedCableTypes: ['power', 'ground']
        }
      ]
    },
    wall_gas_socket: {
      boundingBox_mm: { w: 400, l: 120, h: 600 },
      connectionSockets: [
        {
          id: 'wall_gas_outlet',
          label: 'Gas Outlet',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'wall',
          allowedCableTypes: ['air', 'n2', 'vacuum'],
          offsetDirection: 1
        }
      ]
    },
    wall_feedthrough: {
      boundingBox_mm: { w: 400, l: 120, h: 600 },
      connectionSockets: [
        {
          id: 'feedthrough_room',
          label: 'Feedthrough (Room Side)',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'wall',
          allowedCableTypes: ALL_CABLE_TYPES,
          offsetDirection: 1
        },
        {
          id: 'feedthrough_service',
          label: 'Feedthrough (Service Side)',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'wall',
          allowedCableTypes: ALL_CABLE_TYPES,
          offsetDirection: -1
        }
      ]
    },
    wall_air_barb: {
      boundingBox_mm: { w: 260, l: 90, h: 220 },
      connectionSockets: [
        {
          id: 'wall_air_barb',
          label: 'Air Barb',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'wall',
          allowedCableTypes: ['air'],
          offsetDirection: 1
        }
      ]
    },
    thermostat_wall: {
      boundingBox_mm: { w: 180, l: 80, h: 220 },
      connectionSockets: [
        {
          id: 'thermostat_power',
          label: 'Thermostat Power',
          anchor: { u: 0.5, v: 0.5, w: 0.65 },
          surface: 'wall',
          allowedCableTypes: ['power'],
          offsetDirection: 1
        },
        {
          id: 'thermostat_data',
          label: 'Thermostat Data',
          anchor: { u: 0.5, v: 0.5, w: 0.35 },
          surface: 'wall',
          allowedCableTypes: ['ethernet'],
          offsetDirection: 1
        }
      ]
    },
    thermostat_ceiling: {
      boundingBox_mm: { w: 240, l: 240, h: 120 },
      connectionSockets: [
        {
          id: 'thermostat_ceiling_power',
          label: 'Ceiling Thermostat Power',
          anchor: { u: 0.5, v: 0.5, w: 0.8 },
          surface: 'ceiling',
          allowedCableTypes: ['power']
        },
        {
          id: 'thermostat_ceiling_data',
          label: 'Ceiling Thermostat Data',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'ceiling',
          allowedCableTypes: ['ethernet']
        }
      ]
    },
    chiller: {
      boundingBox_mm: { w: 1200, l: 800, h: 1400 },
      connectionSockets: [
        {
          id: 'chiller_power',
          label: 'Chiller Power',
          anchor: { u: 0.2, v: 0.5, w: 0.2 },
          surface: 'floor',
          allowedCableTypes: ['power', 'ground']
        },
        {
          id: 'chiller_water',
          label: 'Chiller Water Return',
          anchor: { u: 0.8, v: 0.5, w: 0.2 },
          surface: 'floor',
          allowedCableTypes: ['water']
        },
        {
          id: 'chiller_network',
          label: 'Chiller Network',
          anchor: { u: 0.5, v: 0.5, w: 0.5 },
          surface: 'floor',
          allowedCableTypes: ['ethernet']
        }
      ]
    },
    n2_bottle: {
      boundingBox_mm: { w: 450, l: 450, h: 1500 },
      connectionSockets: [
        {
          id: 'n2_bottle_regulator',
          label: 'N2 Regulator',
          anchor: { u: 0.5, v: 0.5, w: 0.9 },
          surface: 'floor',
          allowedCableTypes: ['n2']
        }
      ]
    },
    bottled_air_line: {
      boundingBox_mm: { w: 600, l: 600, h: 1100 },
      connectionSockets: [
        {
          id: 'bottled_air_supply',
          label: 'Bottled Air Supply',
          anchor: { u: 0.5, v: 0.5, w: 0.8 },
          surface: 'floor',
          allowedCableTypes: ['air']
        }
      ]
    },
    table_resizable: {
      boundingBox_mm: { w: 2000, l: 1000, h: 900 },
      connectionSockets: [
        {
          id: 'table_resizable_power',
          label: 'Table Power',
          anchor: { u: 0.5, v: 0.5, w: 0.1 },
          surface: 'floor',
          allowedCableTypes: ['power', 'ground', 'ethernet']
        }
      ]
    }
  };

  const DEFAULT_CABLE_CATALOG = {
    cableTypes: DEFAULT_CABLE_TYPES,
    assets: DEFAULT_ASSET_CATALOG
  };

  function normalizeCableCatalogWithDefaults(candidate) {
    const base = candidate && typeof candidate === 'object' ? candidate : {};
    const cableTypes = Object.assign({}, DEFAULT_CABLE_CATALOG.cableTypes, base.cableTypes || {});
    const assets = Object.assign({}, DEFAULT_CABLE_CATALOG.assets, base.assets || {});
    return Object.assign({}, base, { cableTypes, assets });
  }

  function getDefaultCableColor(type) {
    const meta = DEFAULT_CABLE_CATALOG.cableTypes[type];
    return (meta && meta.color) || '#94a3b8';
  }

  global.DEFAULT_CABLE_CATALOG = DEFAULT_CABLE_CATALOG;
  global.normalizeCableCatalogWithDefaults = normalizeCableCatalogWithDefaults;
  global.getDefaultCableColor = getDefaultCableColor;
})(typeof window !== 'undefined' ? window : globalThis);

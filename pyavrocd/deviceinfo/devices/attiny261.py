
from pymcuprog.deviceinfo.eraseflags import ChiperaseEffect

DEVICE_INFO = {
    'name': 'attiny261',
    'architecture': 'avr8',

    # eeprom
    'eeprom_address_byte': 0x0000,
    'eeprom_size_bytes': 0x0080,
    'eeprom_page_size_bytes': 0x04,
    'eeprom_read_size_bytes': 0x01,
    'eeprom_write_size_bytes': 0x01,
    'eeprom_chiperase_effect': ChiperaseEffect.CONDITIONALLY_ERASED_AVR,
    'eeprom_isolated_erase': False,

    # flash
    'flash_address_byte': 0x0000,
    'flash_size_bytes': 0x0800,
    'flash_page_size_bytes': 0x20,
    'flash_read_size_bytes': 0x02,
    'flash_write_size_bytes': 0x20,
    'flash_chiperase_effect': ChiperaseEffect.ALWAYS_ERASED,
    'flash_isolated_erase': False,

    # fuses
    'fuses_address_byte': 0,
    'fuses_size_bytes': 0x0003,
    'fuses_page_size_bytes': 0x01,
    'fuses_read_size_bytes': 0x01,
    'fuses_write_size_bytes': 0x01,
    'fuses_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'fuses_isolated_erase': False,

    # internal_sram
    'internal_sram_address_byte': 0x0060,
    'internal_sram_size_bytes': 0x0080,
    'internal_sram_page_size_bytes': 0x01,
    'internal_sram_read_size_bytes': 0x01,
    'internal_sram_write_size_bytes': 0x01,
    'internal_sram_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'internal_sram_isolated_erase': False,

    # lockbits
    'lockbits_address_byte': 0,
    'lockbits_size_bytes': 0x0001,
    'lockbits_page_size_bytes': 0x01,
    'lockbits_read_size_bytes': 0x01,
    'lockbits_write_size_bytes': 0x01,
    'lockbits_chiperase_effect': ChiperaseEffect.ALWAYS_ERASED,
    'lockbits_isolated_erase': False,

    # signatures
    'signatures_address_byte': 0,
    'signatures_size_bytes': 3,
    'signatures_page_size_bytes': 0x01,
    'signatures_read_size_bytes': 0x01,
    'signatures_write_size_bytes': 0x00,
    'signatures_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'signatures_isolated_erase': False,

    # Some extra AVR specific fields
    'address_size': '16-bit',
    'ocd_rev' : 1,
    'ocd_base' : 0x20,
    'eear_base' : 0x1E,
    'eear_size' : 2,
    'eecr_base' : 0x1C,
    'eedr_base' : 0x1D,
    'spmcsr_base' : 0x57,
    'osccal_base' : 0x51,
    'dwen_mask' : 0x40,
    'masked_registers' : [0x40],
    'device_id': 0x1E910C,
    'interface': 'ISP+HVPP+debugWIRE'
}
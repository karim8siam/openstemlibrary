import json

# ==========================================
# UNIT 7: Semiconductor Memory Architectures: SRAM, DRAM & Non-Volatile
# ==========================================
u7 = {
    "unitNumber": 7,
    "unitId": "unit7-semiconductor-memory",
    "title": "Semiconductor Memory Architectures: SRAM, DRAM & Non-Volatile",
    "description": "Solid-state digital data storage architectures and device physics: memory organization, word length, bit capacity, 2D/3D matrix addressing, row/column address strobes (RAS/CAS); Static RAM (SRAM) 6-transistor (6T) CMOS bistable cell, precharge lines, read/write stability, and differential sense amplifiers; Dynamic RAM (DRAM) 1-transistor 1-capacitor (1T-1C) trench/stacked cell, destructive readout, capacitive leakage, and periodic refresh scheduling; Non-volatile memory technologies: Mask ROM, fuse PROM, UV-erasable EPROM, floating-gate tunneling EEPROM, and multi-level cell NAND/NOR Flash; SDRAM, DDR protocols, and multi-level cache memory hierarchy.",
    "sections": [
        {
            "id": "dig-7-1",
            "title": "Memory Organization, Matrix Addressing & Decoders",
            "content": r"""<h4>1. General Memory Architecture & Density Classification</h4>
<p>A digital semiconductor memory stores binary data in a regular two-dimensional grid of binary memory cells. The overall storage capacity is expressed as:</p>
<div class="math-display">
$$\text{Capacity} = M \times N \quad (M \text{ words, each of } N \text{ bits})$$
</div>
<p>To access an individual word among $M = 2^k$ addressable locations, the memory requires $k$ binary address input lines ($A_{k-1}, \dots, A_0$). For example, a $64\text{ K} \times 8$ memory chip possesses $2^{16} = 65,536$ words of 8 bits each, requiring $k = 16$ address lines, 8 bidirectional data lines ($D_7 - D_0$), and control lines: Chip Select ($\overline{CS}$), Output Enable ($\overline{OE}$), and Write Enable ($\overline{WE}$).</p>

<h4>2. 2D Matrix Addressing & Row/Column Decoders</h4>
<p>If $2^k$ words were laid out in a single linear column, the required address decoder would have $2^k$ output lines—requiring an astronomical number of gates ($65,536$ outputs for $k=16$). To achieve high physical density and compact square silicon layouts, memory arrays utilize <strong>2D Matrix Coincident Addressing</strong>:</p>
<ol>
<li>The $k$ address bits are split into $r$ Row Address bits and $c$ Column Address bits ($k = r + c$).</li>
<li>The <strong>Row Decoder</strong> activates exactly one horizontal <strong>Word-Line (WL)</strong> among $2^r$ rows, simultaneously enabling all $2^c$ storage cells along that row.</li>
<li>The activated cells place their stored charges onto vertical <strong>Bit-Lines (BL)</strong>.</li>
<li>The <strong>Column Decoder</strong> controls a bank of column pass-gates (multiplexers) that route the selected bit-line data to the chip's output buffers.</li>
</ol>
<p>A $64\text{ K}$-bit array arranged as a $256 \times 256$ matrix requires only one 8-to-256 row decoder and one 8-to-256 column decoder (512 total outputs instead of 65,536).</p>"""
        },
        {
            "id": "dig-7-2",
            "title": "Static RAM (SRAM): The 6T CMOS Memory Cell",
            "simulation": "dig-sram-cell-sim",
            "content": r"""<h4>1. Structure of the 6-Transistor (6T) CMOS SRAM Cell</h4>
<p>Static RAM (SRAM) retains stored data indefinitely as long as DC power is maintained ($V_{DD} > 0$), without requiring periodic refresh cycles. The canonical <strong>6T CMOS SRAM cell</strong> comprises:</p>
<ul>
<li>Two cross-coupled CMOS inverters ($M_1, M_2, M_3, M_4$) forming a bistable latch with complementary internal storage nodes $Q$ and $\bar{Q}$.</li>
<li>Two nMOS access pass-transistors ($M_5, M_6$) connecting nodes $Q$ and $\bar{Q}$ to complementary bit-lines ($BL$ and $\overline{BL}$), gated by Word-Line ($WL$).</li>
</ul>

<h4>2. Operational Cycles of the 6T Cell</h4>
<ol>
<li><strong>Read Cycle:</strong>
<ol>
<li>Precharge phase: Both $BL$ and $\overline{BL}$ are precharged to $V_{DD}$ (or $V_{DD}/2$) and then floated.</li>
<li>Assertion phase: Word-line $WL$ is driven HIGH, turning on access transistors $M_5$ and $M_6$.</li>
<li>Discharge phase: If $Q=0$ and $\bar{Q}=1$, node $Q$ discharges $BL$ through pull-down transistor $M_1$, creating a differential voltage swing $\Delta V = V_{BLB} - V_{BL} \approx 100 - 200\text{ mV}$.</li>
<li>Sensing phase: A sensitive analog <strong>differential sense amplifier</strong> strobes, detecting $\Delta V$ and amplifying it rapidly to full CMOS logic levels ($0\text{ V}$ or $V_{DD}$).</li>
</ol></li>
<li><strong>Write Cycle:</strong>
<ol>
<li>Strong write drivers overdrive $BL$ and $\overline{BL}$ to opposite supply rails (e.g., $BL = 0\text{ V}, \overline{BL} = V_{DD}$ to write a 0).</li>
<li>$WL$ is asserted HIGH. The strong pull-down on $BL$ overpowers the weaker internal pMOS pull-up transistor, flipping the cross-coupled latch into the new state.</li>
</ol></li>
</ol>
<p><strong>Cell Sizing (Read Stability & Write Margin):</strong> To prevent the cell from accidentally flipping its state during a read operation (read disturbance), pull-down transistors $M_1, M_3$ must be made stronger than access transistors $M_5, M_6$ ($\beta_{\text{pull-down}} / \beta_{\text{access}} \ge 1.2 - 1.5$). Conversely, to ensure data can be written successfully, access transistors must be stronger than pull-up transistors $M_2, M_4$ ($\beta_{\text{access}} / \beta_{\text{pull-up}} \ge 1.0$).</p>"""
        },
        {
            "id": "dig-7-3",
            "title": "Dynamic RAM (DRAM): The 1T-1C Cell & Refresh Scheduling",
            "simulation": "dig-dram-refresh-sim",
            "content": r"""<h4>1. The 1-Transistor 1-Capacitor (1T-1C) DRAM Cell</h4>
<p>Robert Dennard (IBM, 1968) patented the <strong>1T-1C DRAM cell</strong>, which slashed silicon area from 6 transistors down to a single access transistor $M$ and an integrated storage capacitor $C_s$ ($C_s \approx 25 - 35\text{ fF}$):</p>
<ul>
<li>Logic '1' is stored as a packet of charge on $C_s$ ($V_C \approx V_{DD}$).</li>
<li>Logic '0' is stored as discharged state ($V_C \approx 0\text{ V}$).</li>
</ul>
<p>Because the cell area is minuscule ($4F^2 - 6F^2$, where $F$ is the lithographic feature size), DRAM achieves gigabit storage densities orders of magnitude higher than SRAM, making it the universal choice for computer main system memory.</p>

<h4>2. Charge Sharing & Destructive Readout</h4>
<p>When Word-Line $WL$ is asserted during a read operation, the storage capacitor $C_s$ shares its charge with the much larger parasitic capacitance of the long bit-line $C_{BL}$ ($C_{BL} \sim 100 - 300\text{ fF} \approx 10 C_s$):</p>
<div class="math-display">
$$V_{\text{final}} = \frac{C_{BL} V_{\text{precharge}} + C_s V_C}{C_{BL} + C_s}$$
</div>
<p>Precharging the bit-line to $V_{DD}/2$ produces a minute voltage perturbation:</p>
<div class="math-display">
$$\Delta V = \pm \frac{C_s}{C_{BL} + C_s} \left(\frac{V_{DD}}{2}\right) \approx \pm 100 - 150\text{ mV}$$
</div>
<p>A cross-coupled regenerative sense amplifier detects $\Delta V$ and swings the bit-line fully to $V_{DD}$ or $0\text{ V}$. Because charge sharing partially discharges $C_s$, the readout is <strong>destructive</strong>. The sense amplifier must immediately rewrite the amplified logic level back into $C_s$ before closing the word-line (Restore Cycle).</p>

<h4>3. Capacitor Leakage & Periodic Refresh Scheduling</h4>
<p>Due to subthreshold MOSFET leakage and reverse-biased $p$-$n$ junction leakage currents, charge leaks off $C_s$ with a time constant of tens of milliseconds. To prevent catastrophic data loss, every row of the DRAM array must be read and rewritten (<strong>refreshed</strong>) periodically (typically every $64\text{ ms}$ at $85^\circ\text{C}$):</p>
<div class="math-display">
$$t_{\text{refresh interval}} \le 64\text{ ms}$$
</div>
<p>Modern DRAM controllers interleave <em>Distributed Auto-Refresh</em> or <em>Self-Refresh</em> commands between normal read/write cycles, consuming less than $1 - 2\%$ of total memory bus bandwidth.</p>"""
        },
        {
            "id": "dig-7-4",
            "title": "Non-Volatile Memories: ROM, PROM, EPROM, EEPROM & Flash",
            "content": r"""<h4>1. Read-Only Memory (ROM) Evolution</h4>
<p>Non-volatile semiconductor memories retain stored data indefinitely without requiring power supplies:</p>
<ol>
<li><strong>Mask ROM:</strong> Data is permanently hardwired during wafer fabrication using a custom photolithographic contact mask. Highest density and lowest cost per bit in mass production, but zero programmability.</li>
<li><strong>Programmable ROM (PROM):</strong> Fabricated with microscopic Nichrome or polycrystalline silicon fuses in series with each memory cell. Programmed once by blowing selected fuses using high-current pulses (One-Time Programmable - OTP).</li>
<li><strong>Erasable PROM (UV-EPROM):</strong> Utilizes a <strong>Floating-Gate MOSFET (FGMOS)</strong> with a completely isolated conductive polysilicon gate embedded inside silicon dioxide dielectric. High-voltage pulses ($V_{PP} \approx 12 - 21\text{ V}$) inject electrons onto the floating gate via <strong>Hot-Carrier Injection (HCI)</strong>. Stored electrons shift the transistor's threshold voltage ($V_t$), programming it to state 0. Erased by shining ultraviolet light ($254\text{ nm}$) through a quartz window on the chip package for 20 minutes, exciting electrons over the $\text{SiO}_2$ potential barrier.</li>
<li><strong>Electrically Erasable PROM (EEPROM):</strong> Employs ultra-thin tunnel oxide ($d_{\text{ox}} < 10\text{ nm}$) beneath the floating gate, enabling bidirectional electrical erasure via <strong>Fowler-Nordheim (F-N) Quantum Mechanical Tunneling</strong>. Can be erased and reprogrammed byte-by-byte in circuit.</li>
</ol>

<h4>2. Modern Flash Memory: NAND vs NOR Architectures</h4>
<p>Invented by Fujio Masuoka (Toshiba, 1984), Flash memory erases blocks of cells simultaneously in a single flash operation via Fowler-Nordheim tunneling:</p>
<div class="table-responsive">
<table class="table table-bordered">
<thead>
<tr><th>Attribute</th><th>NOR Flash</th><th>NAND Flash</th></tr>
</thead>
<tbody>
<tr><td><strong>Cell Interconnection</strong></td><td>Parallel (like NOR gate)</td><td>Series strings of 32 to 128 cells (like NAND gate)</td></tr>
<tr><td><strong>Random Access Speed</strong></td><td>Very Fast ($50 - 80\text{ ns}$)</td><td>Slow initial access ($25\text{ \mu s}$)</td></tr>
<tr><td><strong>Serial Throughput</strong></td><td>Moderate</td><td>Extremely High ($> 1\text{ GB/s}$)</td></tr>
<tr><td><strong>Cell Area Density</strong></td><td>Large ($10F^2$)</td><td>Extremely Compact ($4F^2$, 3D vertical stacked $> 200$ layers)</td></tr>
<tr><td><strong>Primary Application</strong></td><td>BIOS, Router Firmware (eXecute-In-Place)</td><td>Solid-State Drives (SSDs), USB drives, Smartphones</td></tr>
</tbody>
</table>
</div>"""
        },
        {
            "id": "dig-7-5",
            "title": "Advanced Memory Architectures: SDRAM, DDR & Cache Hierarchy",
            "content": r"""<h4>1. Synchronous DRAM (SDRAM) & Double Data Rate (DDR)</h4>
<p>Early asynchronous DRAMs required address strobe handshakes ($\overline{RAS}, \overline{CAS}$) that bottlenecked high-speed microprocessors. <strong>Synchronous DRAM (SDRAM)</strong> synchronizes all control, address, and data lines to the master CPU system clock using internal pipelining and multi-bank prefetching.</p>
<p><strong>Double Data Rate (DDR) SDRAM:</strong> Transfers data on <strong>both the rising and falling edges</strong> of each clock cycle, doubling throughput at identical clock frequencies:</p>
<ul>
<li><strong>DDR1:</strong> 2-bit prefetch buffer (2 data words per clock cycle).</li>
<li><strong>DDR2:</strong> 4-bit prefetch buffer.</li>
<li><strong>DDR3:</strong> 8-bit prefetch buffer.</li>
<li><strong>DDR4:</strong> 16-bit prefetch buffer with independent memory bank groups.</li>
<li><strong>DDR5:</strong> Dual 32-bit channels per module, on-die ECC, data transfer rates exceeding $6400\text{ MT/s}$.</li>
</ul>

<h4>2. Multi-Level Cache Memory Hierarchy</h4>
<p>Because processor execution speed ($3 - 5\text{ GHz}$, sub-nanosecond cycles) is orders of magnitude faster than DRAM latency ($50 - 70\text{ ns}$), modern computer architecture incorporates a multi-tiered cache hierarchy exploiting the <strong>Principle of Locality</strong> (Temporal and Spatial):</p>
<div class="math-display">
\text{CPU Core Registers } (< 1\text{ ns}) \longrightarrow \text{L1 Cache (SRAM, } 32\text{ KB}, \sim 1\text{ ns}) \longrightarrow \text{L2 Cache (SRAM, } 512\text{ KB}, \sim 4\text{ ns}) \longrightarrow \text{L3 Cache (SRAM, } 32\text{ MB}, \sim 12\text{ ns}) \longrightarrow \text{Main Memory (DRAM, } 32\text{ GB}, \sim 60\text{ ns}) \longrightarrow \text{Secondary Storage (NVMe SSD)}
</div>
<p>The <strong>Average Memory Access Time (AMAT)</strong> is:</p>
<div class="math-display">
$$\text{AMAT} = t_{\text{hit}} + \text{Miss Rate} \times \text{Miss Penalty}$$
</div>"""
        }
    ],
    "problems": [
        {
            "id": "dig-p-7-1",
            "title": "Design of a 64 KB Memory Subsystem Using 16 KB x 8 SRAM Chips",
            "statement": "Design a $64\\text{ KB}$ ($65,536 \\text{ bytes}$) microprocessor memory subsystem using standard $16\\text{ KB} \\times 8$ SRAM memory chips. (a) Determine the number of memory chips required. (b) Calculate the total number of address bus lines required for the subsystem and how many address lines connect directly to each chip. (c) Design the chip-select address decoding circuit using a 2-to-4 binary decoder and specify the hexadecimal address range for each memory block.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Chip Count",
                    "math": r"N_{\text{chips}} = \frac{\text{Total Capacity}}{\text{Chip Capacity}} = \frac{64\text{ KB}}{16\text{ KB}} = 4 \text{ memory chips}",
                    "explanation": "Four 16 KB x 8 chips are required to synthesize 64 KB."
                },
                {
                    "stepName": "Step 2: Partition Address Bus Lines",
                    "math": r"64\text{ KB} = 2^{16} \implies 16 \text{ total address lines } (A_{15} - A_0). \quad 16\text{ KB} = 2^{14} \implies 14 \text{ address lines } (A_{13} - A_0) \text{ connect to each chip}",
                    "explanation": "Address lines A0 through A13 connect in parallel to all 4 chips to select a byte within each chip."
                },
                {
                    "stepName": "Step 3: Design Decoder for Chip Select",
                    "math": r"\text{Remaining higher address lines } (A_{15}, A_{14}) \text{ connect to a 2-to-4 line active-LOW decoder to drive } \overline{CS}_0, \overline{CS}_1, \overline{CS}_2, \overline{CS}_3",
                    "explanation": "A 2-to-4 decoder decodes A15 and A14 to enable one of the four chips."
                },
                {
                    "stepName": "Step 4: Determine Hexadecimal Memory Address Ranges",
                    "math": r"\begin{aligned} \text{Chip 0 } (A_{15}A_{14}=00): \ & 0000_{16} \text{ to } 3\text{FFF}_{16} \ (16,384 \text{ bytes}) \\ \text{Chip 1 } (A_{15}A_{14}=01): \ & 4000_{16} \text{ to } 7\text{FFF}_{16} \\ \text{Chip 2 } (A_{15}A_{14}=10): \ & 8000_{16} \text{ to } \text{BFFF}_{16} \\ \text{Chip 3 } (A_{15}A_{14}=11): \ & \text{C}000_{16} \text{ to } \text{FFFF}_{16} \end{aligned}",
                    "explanation": "List continuous address space from 0000H to FFFFH."
                }
            ],
            "answer": "N_{\\text{chips}} = 4; \\quad 16 \\text{ total address lines } (A_{13}-A_0 \\text{ to chips}, \\ A_{15}-A_{14} \\text{ to 2:4 decoder}); \\quad \\text{Range: } 0000_{16} - \\text{FFFF}_{16}"
        },
        {
            "id": "dig-p-7-2",
            "title": "DRAM Refresh Frequency, Time Overhead and Bandwidth Loss",
            "statement": "An $8\\text{ Gb}$ DDR4 DRAM memory chip is organized internally into $8192$ rows. All $8192$ rows must be refreshed within a maximum retention window of $t_{\\text{ret}} = 64.0\\text{ ms}$. Each individual row refresh cycle takes $t_{RC} = 45.0\\text{ ns}$. (a) Calculate the average refresh frequency (how often a refresh command must be issued). (b) Calculate the total time consumed per $64\\text{ ms}$ interval solely for refreshing. (c) Determine the percentage of memory bandwidth lost to refresh operations.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Refresh Command Interval",
                    "math": r"t_{\text{REFI}} = \frac{t_{\text{ret}}}{N_{\text{rows}}} = \frac{64.0 \times 10^{-3}\text{ s}}{8192} \approx 7.8125 \times 10^{-6}\text{ s} = 7.81\text{ \mu s}",
                    "explanation": "A refresh command must be executed every 7.81 microseconds."
                },
                {
                    "stepName": "Step 2: Calculate Total Time Spent Refreshing per 64 ms",
                    "math": r"t_{\text{refresh, total}} = N_{\text{rows}} \times t_{RC} = 8192 \times (45.0 \times 10^{-9}\text{ s}) \approx 3.6864 \times 10^{-4}\text{ s} = 368.64\text{ \mu s}",
                    "explanation": "Multiply number of rows by row cycle time."
                },
                {
                    "stepName": "Step 3: Calculate Bandwidth Overhead Percentage",
                    "math": r"\text{Overhead} = \frac{t_{\text{refresh, total}}}{t_{\text{ret}}} \times 100\% = \frac{368.64\text{ \mu s}}{64,000\text{ \mu s}} \times 100\% \approx 0.576\%",
                    "explanation": "Refresh consumes only 0.58% of total memory bandwidth."
                }
            ],
            "answer": "t_{\\text{REFI}} = 7.81\\text{ \\mu s}, \\quad t_{\\text{total}} = 368.6\\text{ \\mu s per } 64\\text{ ms}, \\quad \\text{Bandwidth Overhead} = 0.576\\%"
        },
        {
            "id": "dig-p-7-3",
            "title": "Average Memory Access Time (AMAT) in Multi-Level Cache Hierarchy",
            "statement": "A modern computer architecture features a two-level cache hierarchy: Level 1 ($L_1$) cache has an access time of $t_1 = 1.20\\text{ ns}$ and a hit rate of $H_1 = 94.0\\%$; Level 2 ($L_2$) cache has an access time of $t_2 = 6.00\\text{ ns}$ and a local hit rate of $H_2 = 85.0\\%$; Main DRAM memory has an access latency of $t_{MM} = 55.0\\text{ ns}$. (a) Calculate the global miss rate for the cache system. (b) Calculate the Average Memory Access Time (AMAT) of the processor. (c) By what factor would memory performance degrade if the caches were eliminated?",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Global Miss Rate",
                    "math": r"\text{Miss Rate}_1 = 1 - 0.940 = 0.060. \quad \text{Global Miss Rate} = \text{Miss Rate}_1 \times (1 - H_2) = 0.060 \times (1 - 0.850) = 0.060 \times 0.150 = 0.0090 \ (0.90\%)",
                    "explanation": "Only 0.9% of memory requests reach main DRAM."
                },
                {
                    "stepName": "Step 2: Calculate Average Memory Access Time (AMAT)",
                    "math": r"\text{AMAT} = t_1 + \text{Miss Rate}_1 \times [t_2 + (1 - H_2) \times t_{MM}] = 1.20 + 0.060 \times [6.00 + 0.150 \times 55.0]\text{ ns}",
                    "explanation": "Formulate multi-level AMAT equation."
                },
                {
                    "stepName": "Step 3: Evaluate AMAT",
                    "math": r"\text{AMAT} = 1.20 + 0.060 \times [6.00 + 8.25] = 1.20 + 0.060 \times (14.25) = 1.20 + 0.855 = 2.055\text{ ns}",
                    "explanation": "Average access time is only 2.06 ns."
                },
                {
                    "stepName": "Step 4: Compute Degradation Factor Without Caches",
                    "math": r"\text{Degradation} = \frac{t_{MM}}{\text{AMAT}} = \frac{55.0\text{ ns}}{2.055\text{ ns}} \approx 26.8 \times",
                    "explanation": "Without caches, memory access would be nearly 27 times slower!"
                }
            ],
            "answer": "\\text{Global Miss Rate} = 0.90\\%, \\quad \\text{AMAT} = 2.055\\text{ ns}, \\quad \\text{Speedup over Raw DRAM: } 26.8\\times"
        }
    ]
}

# ==========================================
# UNIT 8: Integrated Circuit (IC) Technology & Silicon VLSI Microfabrication
# ==========================================
u8 = {
    "unitNumber": 8,
    "unitId": "unit8-ic-technology-fabrication",
    "title": "Integrated Circuit (IC) Technology & Silicon VLSI Microfabrication",
    "description": "Solid-state microfabrication physics and silicon cleanroom processing: classification of integrated circuits (SSI, MSI, LSI, VLSI, ULSI); single-crystal silicon ingot preparation via the Czochralski (CZ) pulling method, wafer slicing, and chemical-mechanical planarization (CMP); epitaxial layer growth; thermal oxidation kinetics and the Deal-Grove model (linear-parabolic regimes); photolithographic pattern transfer, optical diffraction limits, deep ultraviolet (DUV), and extreme ultraviolet (EUV); impurity doping via thermal furnace diffusion (Fick's laws) versus high-energy ion implantation (LSS range theory); metallization, electromigration, vias, and packaging; complete monolithic fabrication sequences for planar NPN bipolar transistors and CMOS inverters, integrated resistors, MOS capacitors, and sheet resistance R_s.",
    "sections": [
        {
            "id": "dig-8-1",
            "title": "Silicon Crystal Growth, Czochralski Ingot Pulling & Wafers",
            "content": r"""<h4>1. Classification of Integrated Circuits</h4>
<p>An <strong>Integrated Circuit (IC)</strong> is a complete electronic circuit fabricated as a single monolithic block on a thin planar substrate of single-crystal silicon. Integration density has expanded exponentially across decades (Moore's Law):</p>
<ul>
<li><strong>Small-Scale Integration (SSI, 1960s):</strong> $< 12$ equivalent logic gates (e.g., 7400 quad NAND gate).</li>
<li><strong>Medium-Scale Integration (MSI, late 1960s):</strong> $12 - 100$ gates (e.g., counters, decoders, 4-bit adders).</li>
<li><strong>Large-Scale Integration (LSI, 1970s):</strong> $100 - 10,000$ gates (e.g., 8-bit microprocessors like Intel 8080, early RAMs).</li>
<li><strong>Very Large-Scale Integration (VLSI, 1980s):</strong> $10,000 - 1,000,000$ gates.</li>
<li><strong>Ultra Large-Scale Integration (ULSI / Modern Nanoscale):</strong> $> 10^{9} - 10^{11}$ transistors on a single $200\text{ mm}^2$ chip (e.g., multi-core CPUs, GPUs with 80+ billion transistors).</li>
</ul>

<h4>2. Electronic Grade Silicon (EGS) & The Czochralski (CZ) Method</h4>
<p>Microfabrication begins with raw quartzite sand ($\text{SiO}_2$), reduced in an electric arc furnace to Metallurgical Grade Silicon (MGS, $\sim 98\%$ pure). Chemical chlorination produces gaseous trichlorosilane ($\text{SiHCl}_3$), which is fractionally distilled and reduced with hydrogen to synthesize polycrystalline <strong>Electronic Grade Silicon (EGS)</strong> with impurity levels below <strong>1 part per billion ($< 10^{-9}$)</strong>.</p>
<p>To convert poly-silicon into a dislocation-free single crystal, Jan Czochralski's (1918) crystal pulling method is employed:</p>
<ol>
<li>EGS is melted in a high-purity fused silica crucible at $1420^\circ\text{C}$ in an inert Argon atmosphere. Controlled $p$-type (Boron) or $n$-type (Phosphorus) dopants are added.</li>
<li>A small single-crystal seed of precise crystallographic orientation ($\langle 100 \rangle$ or $\langle 111 \rangle$) is lowered into the melt surface.</li>
<li>The seed crystal is slowly rotated and pulled upward ($1 - 2\text{ mm/min}$). Surface tension and heat extraction cause silicon atoms in the melt to freeze onto the seed in identical crystalline lattice orientation, producing a massive cylindrical single-crystal ingot (boule) up to $300\text{ mm}$ ($12\text{ inches}$) in diameter and weighing over $100\text{ kg}$.</li>
</ol>

<h4>3. Wafer Shaping and Chemical-Mechanical Planarization (CMP)</h4>
<p>The ingot is ground to uniform diameter, flat or notched for crystal orientation alignment, and sliced into thin discs ($775\text{ \mu m}$ thick) using diamond-coated high-speed wire saws. Wafers undergo edge rounding, chemical etching to relieve surface mechanical damage, and multi-stage <strong>Chemical-Mechanical Planarization (CMP)</strong> using colloidal silica slurry to achieve an atomically flat, mirror-polished surface with root-mean-square roughness $< 0.1\text{ nm}$.</p>"""
        },
        {
            "id": "dig-8-2",
            "title": "Epitaxy, Thermal Oxidation & The Deal-Grove Model",
            "simulation": "dig-deal-grove-oxidation-sim",
            "content": r"""<h4>1. Epitaxial Layer Growth</h4>
<p><strong>Epitaxy</strong> (from Greek <em>epi</em> "upon" and <em>taxis</em> "ordered") is the deposition of a thin single-crystal silicon layer ($0.5 - 5\text{ \mu m}$) onto the substrate wafer, continuing the substrate's exact crystalline lattice. Unlike bulk substrates, the epitaxial layer's dopant type and concentration can be tailored with atomic precision. In <strong>Vapor-Phase Epitaxy (VPE)</strong>, silicon tetrachloride gas is reduced at $1200^\circ\text{C}$:</p>
<div class="math-display">
$$\text{SiCl}_4\text{(g)} + 2\text{H}_2\text{(g)} \overset{1200^\circ\text{C}}{\rightleftharpoons} \text{Si(s)} + 4\text{HCl(g)}$$
</div>

<h4>2. Silicon Dioxide ($\text{SiO}_2$) Thermal Oxidation</h4>
<p>Silicon's pre-eminence as the king of semiconductor materials stems from its native oxide: silicon dioxide ($\text{SiO}_2$), a chemically robust, impermeable dielectric insulator with an enormous band gap ($9.0\text{ eV}$), high breakdown electric field ($10^7\text{ V/cm}$), and exceptional dielectric masking properties against chemical dopants.</p>
<p>Wafers are heated in high-temperature quartz tube furnaces ($900 - 1100^\circ\text{C}$):</p>
<ul>
<li><strong>Dry Oxidation:</strong> $\text{Si} + \text{O}_2 \to \text{SiO}_2$. Slower growth rate, but yields ultra-dense oxide with low interface trap density ($\sim 10^{10}\text{ cm}^{-2}$). Used for thin MOSFET gate oxides.</li>
<li><strong>Wet Oxidation (Steam):</strong> $\text{Si} + 2\text{H}_2\text{O} \to \text{SiO}_2 + 2\text{H}_2$. Grows oxide 5 to 10 times faster due to high solubility of $\text{H}_2\text{O}$ in silica. Used for thick field isolation oxides ($300 - 500\text{ nm}$).</li>
</ul>

<h4>3. The Deal-Grove Oxidation Kinetics Model</h4>
<p>Bruce Deal and Andrew Grove (1965) formulated the kinetics of thermal oxidation. As oxide grows to thickness $x_0$, oxidant species must diffuse through the existing oxide layer before reacting at the $\text{Si}\text{-}\text{SiO}_2$ interface:</p>
<div class="math-display">
$$x_0^2 + A x_0 = B(t + \tau)$$
</div>
<p>where $B$ is the parabolic rate constant ($\mu\text{m}^2/\text{hr}$), $B/A$ is the linear rate constant ($\mu\text{m/hr}$), and $\tau$ accounts for any initial oxide layer. Solving the quadratic equation:</p>
<div class="math-display">
$$x_0(t) = \frac{A}{2} \left[ \sqrt{1 + \frac{4B(t + \tau)}{A^2}} - 1 \right]$$
</div>
<ul>
<li><strong>Linear Regime ($t \ll A^2 / 4B$, Thin Oxides):</strong> Growth is limited by chemical reaction rate at the silicon interface:
<div class="math-display">
$$x_0(t) \approx \frac{B}{A}(t + \tau)$$
</div></li>
<li><strong>Parabolic Regime ($t \gg A^2 / 4B$, Thick Oxides):</strong> Growth is limited by diffusion of oxidant molecules through the thick oxide layer:
<div class="math-display">
$$x_0^2(t) \approx B \cdot t \implies x_0(t) \propto \sqrt{t}$$
</div></li>
</ul>"""
        },
        {
            "id": "dig-8-3",
            "title": "Photolithography: Photoresist Chemistry & Pattern Transfer",
            "content": r"""<h4>1. The Photolithographic Process Sequence</h4>
<p><strong>Photolithography</strong> is the optical printing process that transfers microscopic geometric circuit patterns from a photographic mask (reticle) onto the wafer surface:</p>
<ol>
<li><strong>Surface Preparation & HMDS Priming:</strong> Hexamethyldisilazane (HMDS) vapor prime makes the hydrophilic $\text{SiO}_2$ surface hydrophobic to ensure photoresist adhesion.</li>
<li><strong>Spin Coating:</strong> A liquid light-sensitive polymeric <strong>photoresist</strong> is dispensed onto the wafer, spun at $3000 - 5000\text{ RPM}$ to form a uniform thin film ($0.5 - 1.0\text{ \mu m}$).</li>
<li><strong>Soft Bake:</strong> Heated to $90 - 100^\circ\text{C}$ to evaporate solvents.</li>
<li><strong>Mask Alignment & Exposure:</strong> High-precision reduction stepper lenses project UV light through a photomask.
<ul>
<li><strong>Positive Photoresist (Diazoquinone/Novolac):</strong> Exposed regions undergo photochemical scission, becoming highly soluble in alkaline aqueous developer solution. Unexposed regions remain insoluble. Leaves an exact duplicate of the dark mask pattern. Standard in VLSI due to superior resolution.</li>
<li><strong>Negative Photoresist (Polyisoprene):</strong> Exposed regions cross-link and polymerize, becoming insoluble. Leaves the photographic negative. Swells during development, limiting resolution.</li>
</ul></li>
<li><strong>Post-Exposure Bake & Development:</strong> Dissolves soluble resist regions, exposing the underlying $\text{SiO}_2$ film.</li>
<li><strong>Hard Bake ($120 - 140^\circ\text{C}$):</strong> Hardens the resist polymer for etch resistance.</li>
<li><strong>Etching:</strong> Pattern transfer into the underlying material.
<ul>
<li><strong>Wet Chemical Etching:</strong> Buffered Oxide Etch (BOE / HF). Isotropic (etches equally in all directions), producing undesirable lateral undercut.</li>
<li><strong>Dry Plasma / Reactive-Ion Etching (RIE):</strong> High-energy reactive ions in an anisotropic RF plasma etch vertically with near-zero lateral undercut, preserving sub-micron feature fidelity.</li>
</ul></li>
<li><strong>Photoresist Stripping:</strong> Removed via oxygen plasma ashing ($\text{O}_2$ plasma incinerates organic resist to $\text{CO}_2$ and $\text{H}_2\text{O}$).</li>
</ol>

<h4>2. Optical Resolution Limits & EUV Lithography</h4>
<p>The minimum resolvable feature size ($CD$, Critical Dimension) is governed by the Rayleigh diffraction criterion:</p>
<div class="math-display">
$$CD = k_1 \frac{\lambda}{NA}$$
</div>
<p>where $\lambda$ is illumination wavelength, $NA = n\sin\theta$ is numerical aperture, and $k_1$ is a process factor ($\ge 0.25$). Modern semiconductor fabrication transitioned from Mercury arc lamps (G-line $436\text{ nm}$, I-line $365\text{ nm}$) to Excimer lasers (KrF $248\text{ nm}$, ArF $193\text{ nm}$ immersion lithography with water $n=1.44$). For sub-$7\text{ nm}$ nodes, state-of-the-art foundries utilize <strong>Extreme Ultraviolet (EUV)</strong> lithography ($\lambda = 13.5\text{ nm}$) generated by pulsing high-power $\text{CO}_2$ lasers into molten tin droplets in ultra-high vacuum.</p>"""
        },
        {
            "id": "dig-8-4",
            "title": "Doping: Thermal Diffusion vs High-Energy Ion Implantation",
            "content": r"""<h4>1. Thermal Furnace Diffusion</h4>
<p>Impurity doping introduces group-III acceptors (Boron) or group-V donors (Phosphorus, Arsenic) into the silicon crystal lattice. In classical <strong>thermal diffusion</strong>, wafers in a quartz furnace ($900 - 1200^\circ\text{C}$) are exposed to a gaseous dopant source ($\text{POCl}_3, \text{BBr}_3$):</p>
<ol>
<li><strong>Predeposition (Constant Source Diffusion):</strong> Dopant surface concentration is held fixed at solid solubility limit $C_s$. Governed by Fick's Second Law:
<div class="math-display">
$$\frac{\partial C(x,t)}{\partial t} = D \frac{\partial^2 C(x,t)}{\partial x^2}$$
</div>
Boundary conditions ($C(0,t) = C_s, C(\infty,t) = 0$) yield the <strong>Complementary Error Function (erfc)</strong> profile:
<div class="math-display">
$$C(x, t) = C_s \operatorname{erfc}\left( \frac{x}{2 \sqrt{Dt}} \right)$$
</div></li>
<li><strong>Drive-In Diffusion (Limited Source):</strong> Dopant vapor is shut off; the fixed deposited dose $Q$ drives deeper into the silicon at higher temperature, forming a <strong>Gaussian profile</strong>:
<div class="math-display">
$$C(x, t) = \frac{Q}{\sqrt{\pi D t}} \exp\left( - \frac{x^2}{4 D t} \right)$$
</div></li>
</ol>
<p>Thermal diffusion is isotropic: dopants diffuse laterally under mask edges by $70 - 80\%$ of the vertical junction depth ($x_{\text{lat}} \approx 0.8 x_j$), making it obsolete for shallow sub-micron source/drain junctions.</p>

<h4>2. High-Energy Ion Implantation</h4>
<p>The dominant doping technique in modern VLSI. Dopant atoms are ionized in an arc source, accelerated through high electrostatic potential differences ($10\text{ keV} - 3\text{ MeV}$), mass-analyzed using a bending dipole electromagnet to guarantee $100\%$ chemical purity, and fired directly into the silicon wafer.</p>
<p>According to Lindhard-Scharff-Schiøtt (LSS) stopping theory, the dopant profile follows a Gaussian distribution centered at the <strong>Projected Range ($R_p$)</strong> with standard deviation <strong>Projected Straggle ($\Delta R_p$)</strong>:</p>
<div class="math-display">
$$C(x) = \frac{\Phi}{\sqrt{2\pi}\Delta R_p} \exp\left( - \frac{(x - R_p)^2}{2 \Delta R_p^2} \right)$$
</div>
<p>where $\Phi$ is the implanted ion dose (ions/$\text{cm}^2$). The peak concentration occurs at depth $x = R_p$:</p>
<div class="math-display">
$$C_{\text{peak}} = \frac{\Phi}{\sqrt{2\pi}\Delta R_p} \approx \frac{0.3989 \Phi}{\Delta R_p}$$
</div>
<p>Advantages over diffusion: Independent control of depth (via acceleration energy) and dose (via beam current integration); near-zero lateral straggle; room temperature operation; compatibility with photoresist masks.</p>
<p><strong>Post-Implant Thermal Annealing:</strong> High-energy ion bombardment shatters the crystalline silicon lattice into an amorphous layer. Rapid Thermal Annealing (RTA, $1000^\circ\text{C}$ for seconds) recrystallizes the damaged lattice and shifts dopant atoms into substitutional lattice sites where they become electrically active.</p>"""
        },
        {
            "id": "dig-8-5",
            "title": "CMOS Inverter Fabrication Sequence & Sheet Resistance",
            "simulation": "dig-cmos-inverter-fabrication-sim",
            "content": r"""<h4>1. Complete Monolithic CMOS Fabrication Sequence (Self-Aligned Twin-Well)</h4>
<p>Fabricating a complementary pair of nMOS and pMOS transistors on a single substrate requires a sequence of approximately 30 lithographic mask levels:</p>
<ol>
<li><strong>Starting Substrate:</strong> Lightly doped $p$-type $\langle 100 \rangle$ silicon wafer.</li>
<li><strong>Well Formation:</strong> Ion implantation of Phosphorus followed by high-temperature drive-in forms the <strong>$n$-well</strong> (in which pMOS transistors will reside).</li>
<li><strong>Shallow Trench Isolation (STI):</strong> Etch narrow vertical trenches ($300\text{ nm}$ deep) between active transistor areas, fill with CVD $\text{SiO}_2$, and planarize via CMP to eliminate parasitic latchup.</li>
<li><strong>Gate Stack:</strong> Thermally grow ultra-thin gate dielectric ($\text{SiO}_2$ or high-$\kappa$ Hafnium dioxide $\text{HfO}_2$), deposit polycrystalline silicon (polysilicon) or metal gate layer, pattern via lithography, and etch vertical gate electrodes.</li>
<li><strong>Lightly Doped Drain (LDD) Implantation:</strong> Shallow low-dose implants under gate edges suppress hot-carrier degradation.</li>
<li><strong>Dielectric Sidewall Spacers:</strong> Conformally deposit $\text{Si}_3\text{N}_4$ or $\text{SiO}_2$ and anisotropically plasma etch to leave insulating spacer sidewalls along gate edges.</li>
<li><strong>Source/Drain Self-Aligned Implantation:</strong>
<ul>
<li>$n^+$ Implantation (Arsenic/Phosphorus) forms nMOS source/drain regions. The polysilicon gate acts as an impenetrable mask, naturally aligning the channel edges (Self-Aligned Gate).</li>
<li>$p^+$ Implantation (Boron) forms pMOS source/drain regions.</li>
</ul></li>
<li><strong>Salicidation (Self-Aligned Silicide):</strong> Deposit thin Cobalt or Nickel, anneal at $700^\circ\text{C}$ to form low-resistance metal silicide ($\text{NiSi}$) on all exposed silicon contacts and polysilicon gates, reducing contact resistance.</li>
<li><strong>Pre-Metal Dielectric (PMD) & Tungsten Contacts:</strong> Deposit thick planarizing oxide, plasma etch contact vias down to source/drain/gate regions, and fill with refractory Tungsten (W) plugs.</li>
<li><strong>Multi-Level Metallization:</strong> Deposit alternating copper (Cu) interconnect wire layers separated by low-$\kappa$ dielectric insulators using the dual-damascene electroplating process (up to 12 - 15 metal wiring levels).</li>
<li><strong>Passivation & Wire Bonding:</strong> Deposit protective silicon nitride ($\text{Si}_3\text{N}_4$) scratch coat, etch bond pad openings, slice die, mount to ceramic/plastic leadframe, bond gold/copper wires, and encapsulate in epoxy resin.</li>
</ol>

<h4>2. Integrated Passive Components & Sheet Resistance ($R_s$)</h4>
<p>Passive circuit components inside integrated circuits:</p>
<ul>
<li><strong>Diffused Resistors:</strong> A semiconductor layer of length $L$, width $W$, thickness $t$, and resistivity $\rho$ has resistance:
<div class="math-display">
$$R = \rho \frac{L}{A} = \frac{\rho}{t} \left(\frac{L}{W}\right) = R_s \left(\frac{L}{W}\right)$$
</div>
where $R_s = \rho / t$ is the <strong>Sheet Resistance</strong>, expressed in units of <strong>Ohms per square ($\Omega/\square$)</strong>. The ratio $L/W$ represents the number of squares. Right-angle square corners contribute approximately $0.56$ squares each due to current crowding.</li>
<li><strong>MOS Capacitors:</strong> Formed by gate polysilicon electrode over thin dielectric oxide over an $n^+$ diffused silicon bottom plate:
<div class="math-display">
$$C = \frac{\varepsilon_{\text{ox}} \varepsilon_0 A}{t_{\text{ox}}}$$
</div></li>
</ul>"""
        }
    ],
    "problems": [
        {
            "id": "dig-p-8-1",
            "title": "Deal-Grove Thermal Oxidation Thickness in Dry vs Wet Oxygen",
            "statement": "A silicon wafer is oxidized at $1000^\\circ\\text{C}$ starting with an initial native oxide of $x_i = 10\\text{ nm}$ (assume $\\tau \\approx 0$). The Deal-Grove rate constants are: Dry $\\text{O}_2$: $B = 0.0117\\text{ \\mu m}^2/\\text{hr}$, $B/A = 0.070\\text{ \\mu m/hr}$; Wet Steam: $B = 0.287\\text{ \\mu m}^2/\\text{hr}$, $B/A = 0.867\\text{ \\mu m/hr}$. (a) Calculate the parameter $A$ for both dry and wet processes. (b) Calculate the oxide thickness $x_0$ grown after $t = 2.0\\text{ hours}$ in dry $\\text{O}_2$. (c) Calculate the oxide thickness $x_0$ grown after $t = 2.0\\text{ hours}$ in wet steam and evaluate the growth acceleration factor.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Parameter A",
                    "math": r"A = \frac{B}{B/A}. \quad \text{Dry: } A = \frac{0.0117}{0.070} \approx 0.1671\text{ \mu m}. \quad \text{Wet: } A = \frac{0.287}{0.867} \approx 0.3310\text{ \mu m}",
                    "explanation": "Compute A for both oxidation regimes."
                },
                {
                    "stepName": "Step 2: Solve Deal-Grove Equation for Dry Oxidation",
                    "math": r"x_0(t) = \frac{A}{2} \left[ \sqrt{1 + \frac{4 B t}{A^2}} - 1 \right] = \frac{0.1671}{2} \left[ \sqrt{1 + \frac{4(0.0117)(2.0)}{(0.1671)^2}} - 1 \right] = 0.08355 \left[ \sqrt{1 + \frac{0.0936}{0.02793}} - 1 \right]",
                    "explanation": "Substitute numerical values into the quadratic Deal-Grove formula."
                },
                {
                    "stepName": "Step 3: Evaluate Dry Oxide Thickness",
                    "math": r"x_0 = 0.08355 \left[ \sqrt{1 + 3.351} - 1 \right] = 0.08355 [2.086 - 1] = 0.08355 \times 1.086 \approx 0.0907\text{ \mu m} = 90.7\text{ nm}",
                    "explanation": "Dry oxidation yields ~91 nm after 2 hours."
                },
                {
                    "stepName": "Step 4: Solve Deal-Grove Equation for Wet Steam Oxidation",
                    "math": r"x_0 = \frac{0.3310}{2} \left[ \sqrt{1 + \frac{4(0.287)(2.0)}{(0.3310)^2}} - 1 \right] = 0.1655 \left[ \sqrt{1 + \frac{2.296}{0.1096}} - 1 \right] = 0.1655 [\sqrt{21.95} - 1] = 0.1655 [4.685 - 1] \approx 0.6099\text{ \mu m} = 610\text{ nm}",
                    "explanation": "Wet steam yields ~610 nm after 2 hours."
                },
                {
                    "stepName": "Step 5: Compare Acceleration Factor",
                    "math": r"\text{Acceleration} = \frac{609.9\text{ nm}}{90.7\text{ nm}} \approx 6.72 \times",
                    "explanation": "Wet oxidation is 6.7 times thicker than dry oxidation due to the high solubility of H2O in silica."
                }
            ],
            "answer": "x_{\\text{dry}} = 90.7\\text{ nm}, \\quad x_{\\text{wet}} = 610\\text{ nm} \\quad (\\text{Wet Steam is } 6.72\\times \\text{ faster})"
        },
        {
            "id": "dig-p-8-2",
            "title": "Integrated Diffused Resistor Serpentine Layout Design",
            "statement": "An integrated circuit requires a precision diffused resistor of value $R = 8.50\\text{ k}\\Omega$. A $p$-type diffused layer has a measured sheet resistance of $R_s = 40.0\\text{ }\\Omega/\\square$. The minimum design rule lithographic line width is $W = 2.50\\text{ \\mu m}$. The layout is routed in a serpentine geometry incorporating four $90^\\circ$ square corners (each corner contributes $0.56$ effective squares). (a) Calculate the total number of squares required. (b) Determine the effective number of squares in the straight sections. (c) Calculate the total physical length $L$ of the resistor track.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Total Required Squares",
                    "math": r"N_{\text{total squares}} = \frac{R}{R_s} = \frac{8500\text{ }\Omega}{40.0\text{ }\Omega/\square} = 212.5 \text{ squares}",
                    "explanation": "Divide total target resistance by sheet resistance."
                },
                {
                    "stepName": "Step 2: Account for Corner Squares",
                    "math": r"N_{\text{corners}} = 4 \times 0.56 = 2.24 \text{ squares}",
                    "explanation": "Four 90-degree corners contribute 2.24 squares."
                },
                {
                    "stepName": "Step 3: Calculate Squares in Straight Run",
                    "math": r"N_{\text{straight}} = N_{\text{total}} - N_{\text{corners}} = 212.5 - 2.24 = 210.26 \text{ squares}",
                    "explanation": "Subtract corner contribution."
                },
                {
                    "stepName": "Step 4: Calculate Total Length of Straight Runs",
                    "math": r"L_{\text{straight}} = N_{\text{straight}} \times W = 210.26 \times 2.50\text{ \mu m} \approx 525.65\text{ \mu m}",
                    "explanation": "Multiply straight squares by line width."
                },
                {
                    "stepName": "Step 5: Total Centerline Track Length",
                    "math": r"L_{\text{total}} = L_{\text{straight}} + 4 \times W = 525.65 + (4 \times 2.50)\text{ \mu m} = 535.65\text{ \mu m} \approx 536\text{ \mu m}",
                    "explanation": "Centerline length is ~536 micrometers."
                }
            ],
            "answer": "N_{\\text{squares}} = 212.5 \\text{ squares}, \\quad L_{\\text{straight}} = 525.7\\text{ \\mu m}, \\quad L_{\\text{total}} \\approx 536\\text{ \\mu m}"
        },
        {
            "id": "dig-p-8-3",
            "title": "Ion Implantation Peak Concentration and Junction Depth",
            "statement": "Boron ($^{11}\\text{B}$) is ion-implanted at an acceleration energy of $E = 100\\text{ keV}$ into an $n$-type silicon substrate with uniform background doping concentration $N_D = 2.0 \\times 10^{16}\\text{ atoms/cm}^3$. The implant dose is $\\Phi = 4.0 \\times 10^{14}\\text{ cm}^{-2}$. From LSS range tables, the projected range is $R_p = 0.30\\text{ \\mu m}$ ($3.0 \\times 10^{-5}\\text{ cm}$) and the projected straggle is $\\Delta R_p = 0.070\\text{ \\mu m}$ ($7.0 \\times 10^{-6}\\text{ cm}$). (a) Calculate the peak Boron dopant concentration $C_{\\text{peak}}$ at $x = R_p$. (b) Calculate the metallurgical $p$-$n$ junction depth $x_j$ where $C(x_j) = N_D$.",
            "steps": [
                {
                    "stepName": "Step 1: Calculate Peak Concentration at x = R_p",
                    "math": r"C_{\text{peak}} = \frac{\Phi}{\sqrt{2\pi}\Delta R_p} = \frac{4.0 \times 10^{14}\text{ cm}^{-2}}{\sqrt{2\pi}(7.0 \times 10^{-6}\text{ cm})} = \frac{4.0 \times 10^{14}}{1.7545 \times 10^{-5}} \approx 2.28 \times 10^{19}\text{ cm}^{-3}",
                    "explanation": "Evaluate peak concentration at the center of the Gaussian profile."
                },
                {
                    "stepName": "Step 2: Formulate Metallurgical Junction Condition",
                    "math": r"C(x_j) = C_{\text{peak}} \exp\left( - \frac{(x_j - R_p)^2}{2 \Delta R_p^2} \right) = N_D = 2.0 \times 10^{16}\text{ cm}^{-3}",
                    "explanation": "Set Gaussian concentration equal to background substrate doping."
                },
                {
                    "stepName": "Step 3: Solve for Distance from Peak",
                    "math": r"\exp\left( - \frac{(x_j - R_p)^2}{2 \Delta R_p^2} \right) = \frac{2.0 \times 10^{16}}{2.28 \times 10^{19}} \approx 8.77 \times 10^{-4} \implies \frac{(x_j - R_p)^2}{2 \Delta R_p^2} = -\ln(8.77 \times 10^{-4}) \approx 7.039",
                    "explanation": "Take natural logarithm of concentration ratio."
                },
                {
                    "stepName": "Step 4: Calculate Junction Depth x_j",
                    "math": r"|x_j - R_p| = \Delta R_p \sqrt{2 \times 7.039} = (0.070\text{ \mu m}) \times \sqrt{14.078} = 0.070 \times 3.752 \approx 0.263\text{ \mu m}",
                    "explanation": "Multiply straggle by square root factor: 0.263 um beyond peak."
                },
                {
                    "stepName": "Step 5: Final Metallurgical Depth",
                    "math": r"x_j = R_p + 0.263\text{ \mu m} = 0.300 + 0.263 = 0.563\text{ \mu m} = 563\text{ nm}",
                    "explanation": "Add projected range Rp to find junction depth from wafer surface."
                }
            ],
            "answer": "C_{\\text{peak}} = 2.28 \\times 10^{19}\\text{ cm}^{-3}, \\quad x_j = 0.563\\text{ \\mu m} = 563\\text{ nm}"
        }
    ]
}

with open("dig_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7, f, indent=2)
print("dig_u7.json created successfully!")

with open("dig_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8, f, indent=2)
print("dig_u8.json created successfully!")

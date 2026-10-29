---
title: "A Tiny Aluminum Cube: Tinkering with the Beelink ME Pro NAS"
date: 2026-10-09
authors: [vonng]
summary: >
  Four spare hard drives and four NVMe SSDs fit neatly into a Beelink ME Pro. Why I chose it over the Minisforum N5, what assembly and Ubuntu setup involve, and what a NAS with enough CPU power to do more than store files can offer.
tags: [Hardware, Local First, Commentary]
images: [featured.webp]
---
Last night before bed, I threw together a quick post on [the three gadgets middle-aged men obsess over](/en/db/homelab-10g/): NAS boxes, routers, and chargers. It picked up more than 30,000 reads in a single day. Apparently the stereotype holds up.

![WeChat readership statistics for the previous NAS article, showing 30,368 reads](reads.webp)

In that post, I said I would write about my new Beelink ME Pro NAS today. So here I am before bed again, writing about this little aluminum cube. First, the disclosure: nobody paid me for this. I bought all the equipment myself, for my own use.

## How I Ended Up Looking at Beelink

I first noticed Beelink's mini PCs when DHH was promoting Omarchy. He was experimenting with Linux mini PCs, found that Beelink's little boxes were a good fit, and posted enough tweets about them to make me want one. In September 2025, I went through Beelink's lineup and, after much deliberation, bought a GTR9 Pro: an AMD Ryzen AI Max+ 395 with 128 GB of RAM. I wrote about it in [“WinStudio: Running a 200B Model Locally for ¥10,000?”](/ai/local-200b/).

On paper, that machine might have delivered the largest percentage gain of any “investment” I made over the past year: the official retail price climbed from just over ¥10,000 to ¥27,000. I've been very happy with it. It handles builds quickly, runs plenty of test VMs, serves as a build farm for the PostgreSQL extension repository, and stays very quiet. It is much easier to live with than my old Dell PowerEdge R730 server.

My only regret is not buying a few more at the time. Once the RAM price surge pushed the sticker price to ¥27,000, buying another was out of the question, though the rest of the catalog was still worth a look.

## Why Another NAS?

Mini PCs with lots of RAM aren't such good value anymore, but there was another category worth tinkering with: NAS hardware.

Say “NAS” and most people think of Synology, QNAP, or TerraMaster. Over the past couple of years, though, a wave of newcomers has entered the market: Beelink, Minisforum, fnOS, UGREEN, and even Xiaomi.

I have used Synology for years. It charges a steep premium, which is another way of saying you don't get much hardware for your money. Most of that premium pays for DSM, its software. It works out of the box, manages your storage pools, and requires almost no babysitting. If you have the budget and don't want to tinker, Synology is still the best choice.

As I mentioned in yesterday's post, I previously ran a Synology DS918+ alongside a two-bay DS720+. I sold both yesterday and consolidated onto a DS923+ with a 10GbE upgrade. My primary data—the files I cannot afford to lose or corrupt—still lives on that Synology as the authoritative copy. Outside of that, though, I don't mind having a second NAS to experiment with.

The real motivation was simpler: my China Merchants Bank card offers 10× points on my birthday, so I was looking for an excuse to buy something. I came across the ME Pro, did some research, and realized it matched my pile of spare parts exactly: four hard drives and four NVMe SSDs pulled from desktops. With four hard-drive bays and four M.2 slots, it could put every last one of those drives back to work. Why not?

## Minisforum N5 vs. Beelink ME Pro

At first, I was actually leaning toward the Minisforum N5 series. It is another tidy-looking box, with five drive bays. The top-tier N5 Max runs the same AMD Ryzen AI Max+ 395 as my GTR9 Pro. On second thought, though, I already had a machine with that chip; buying a second one made little sense when what I needed here was storage.

![JD listing for the five-bay Minisforum N5 Air, showing a Ryzen 7 255 and a starting price of CNY 3,189](n5.webp)

*The listing advertises PCIe ×16 expansion, 10GbE, and up to 174 TB of storage. The selected option shows 0 GB of memory and 64 GB of system storage, so its starting price isn't directly comparable to my ME Pro purchase.*

The N5 Air and N5 Pro also looked good, and the N5 Pro supports ECC memory. All three share the same enclosure, though, and its size was the dealbreaker. I also didn't have a fifth hard drive. I checked what buying another one to three drives would cost: a 16 TB Seagate IronWolf cost me ¥3,300 in 2022, and JD now lists it at ¥5,900, nearly double. I could do without that fifth bay.

![April 25, 2022 order for two 16 TB Seagate IronWolf hard drives](ironwolf-2022.webp)

*The April 2022 order totals CNY 6,995.40 for two drives; I remember paying roughly CNY 3,300 apiece.*

![Historical JD listing showing one 16 TB Seagate IronWolf at CNY 5,912.26, with a regular price of CNY 5,999](ironwolf-price.webp)

*The price I saw while shopping: CNY 5,912.26 for one 16 TB IronWolf, with a regular price of CNY 5,999.*

The ME Pro has four bays in a tight, space-efficient chassis. Better yet, it matches the exact height of my Synology, so both sit neatly side by side on the same rack shelf. Beelink makes two-bay and four-bay versions, but for any reasonably serious NAS setup, four bays is the baseline.

![September 21, 2026 order confirmation for the four-bay Beelink ME Pro H255, paid CNY 4,819.94](order.webp)

To be fair, the Minisforum N5 is a strong contender. My final shortlist came down to the N5 series and the four-bay Beelink ME Pro. With a government subsidy and a promotion, the ME Pro came out to ¥4,819.

![JD listing for the four-bay Beelink ME Pro H255, with 32 GB of RAM and a 500 GB system drive selected](me-pro-shop.webp)

*The listing shows CNY 5,670.51 for this configuration. The CNY 4,819.94 in the order screenshot is the discounted price I actually paid.*

## Why Beelink Won Out

What tipped the decision to Beelink?

Size was the main factor. The CNC-machined unibody aluminum chassis on the four-bay model measures roughly [165 × 145 × 165 mm without the feet](https://www.bee-link.com.cn/computer-73493777)—remarkably compact, and about as tall as an iPhone Pro Max. I meant to take more photos, but both NAS boxes were busy copying data and I didn't feel like moving them. These shots should give a rough sense of scale.

![Beelink ME Pro sitting beside a Synology NAS and an ASUS ROG tablet on the desk](featured.webp)

![A 12U rack holding laptops, mini PCs, and both NAS units](rack.webp)

![Desk layout with the computers and NAS units before moving them into the rack](desk.webp)

![Overhead view of the computers, NAS units, and cabling on the desk](overhead.webp)

Another thing I like is that the same chassis accommodates several processor platforms. The motherboard sits in a drawer that slides out like a drive tray, so you can swap the entire board assembly. Beelink doesn't appear to sell the boards separately yet, but at least the design leaves room for upgrades. It also makes cleaning out dust much easier.

### Processor and motherboard options

These are the options listed in the comparison. The availability date in the last row is cut off in the screenshot.

| Processor option | Architecture | Typical use |
| --- | --- | --- |
| Loongson 2K3000 | LoongArch (Chinese-developed architecture) | Experimenting with a domestically developed platform |
| Intel N95 / N150 / J5005 | x86 | Entry-level NAS around CNY 1,000 |
| Intel Core i5-13500H | x86 | General-purpose all-in-one PC |
| AMD Ryzen 7 H 255 / HX 370 / HX 470 | x86 | High-performance content creation and storage |
| Core Ultra 5 325H / X7 358H (Panther Lake) | x86 | Upcoming AI NAS; the availability text is cropped |
{.wide .expand}

[Original board-comparison screenshot](boards.webp)

I bought the cheaper Ryzen 7 H 255 model. There are also HX 370 and HX 470 versions and, of all things, a Loongson motherboard option. That leaves plenty to experiment with. I previously helped get [Loongson support into the official PostgreSQL APT repository](/pg/pg-apt-loong64/). If I ever need to work on Loongson support locally, I could just slide a Loongson ME Pro board into this chassis instead of buying another oddball machine.

## Hands-On: Bring a Screwdriver

In person, the hardware is easy to like.

Coming from Synology, though, you will be turning a lot of screws. The rear cover over the drive bays is magnetic and pops right off, but all four internal drive trays are secured with hex screws (an Allen key is tucked into the underside of the chassis). Pulling or installing a drive means backing those screws out and threading them back in every time—far more fiddly than Synology's tool-free snap-in trays.

![Both NAS units with rear covers removed alongside a Bosch Go electric screwdriver](screwdriver.webp)

*With a Bosch Go electric screwdriver in hand, I'm ready for anything.*

The SSDs require some disassembly too. One reason I picked the “low-end” Ryzen 7 H 255 model is that although it has the cheaper CPU, it gets the generous M.2 configuration: four slots in total.

- Two PCIe ×4 slots on the underside of the motherboard;
- One PCIe ×4 slot on top for the system drive;
- One PCIe ×1 slot right next to the system drive, left empty from the factory.

If you only want to add two NVMe drives, opening the bottom cover and undoing two screws is enough. To use the ×1 slot as well, you have to slide out the motherboard drawer, remove three screws from the cooling fan, undo two more on the system-drive cover, and then insert the SSD. A little more work, but surely a middle-aged man can handle a few screws.

## OS Setup: Wipe Windows, Install Ubuntu

There are several configurations to choose from. The cheapest is a barebones unit without RAM or storage for a little over ¥2,000. I bought the version with 32 GB of RAM and a 500 GB system drive for about ¥4,800. After doing the math, the bundled memory worked out cheaper than buying it separately.

The machine ships with Windows 11 Pro preinstalled. I had no use for that, so I wiped the drive immediately and installed Ubuntu.

You can also install fnOS. Friends tell me it is pleasant to use and one of the better third-party NAS operating systems. I didn't feel like tinkering with another system, and I don't need fancy media features. I just need somewhere to put files: configure RAID, export an SMB share, and mount it locally. Ubuntu is enough for that.

If you want a full NAS operating system along the lines of Synology DSM, fnOS may be a better fit. I haven't tested it myself, but my understanding is that Beelink also manufactures fnOS's own branded hardware. That would make this about as close to first-party hardware as you can get.

## PC NAS: A Hybrid Category

Strictly speaking, machines like this aren't traditional NAS appliances anymore. They are closer to a PC and a NAS in one box—call it a “PC NAS.”

Traditional NAS units focus on storage, with barely any CPU power to spare. My three Synology boxes have either a dual-core Ryzen or a quad-core Celeron, paired with 2 to 4 GB of RAM. What can you actually run on such anemic hardware today? Pretty much one thing: file storage.

### What the older Synology hardware can do

There is more to this comparison than four cores versus two. The specifications below draw on Intel's CPU specifications, AMD's R1000 product materials, and GCC architecture-support notes cited in the original comparison.

| CPU specification | DS918+: Celeron J3455 | DS720+: Celeron J4125 | DS923+: Ryzen Embedded R1600 |
| --- | --- | --- | --- |
| Platform / architecture | Intel Apollo Lake | Intel Gemini Lake Refresh | AMD first-generation Zen |
| Process node | 14 nm | 14 nm | 14 nm |
| Physical cores | 4 | 4 | 2 |
| Hardware threads | 4 | 4 | 4, with SMT |
| Base clock | 1.5 GHz | 2.0 GHz | 2.6 GHz |
| Maximum clock | 2.3 GHz | 2.7 GHz | 3.1 GHz |
| Total L2 cache | 2 MB | 4 MB | 1 MB |
| L3 cache | None | None | 4 MB |
| Integrated graphics | Intel HD Graphics 500 | Intel UHD Graphics 600 | None |
| Video acceleration | Intel Quick Sync | Intel Quick Sync | No integrated video transcoding engine |
| AES instructions | Yes | Yes | Yes |
| AVX / AVX2 | No | No | Yes |
| ECC memory support | No | No | Yes |
| Nominal / configurable CPU TDP | 10 W | 10 W | 12–25 W |
{.wide .expand}

[Original CPU-specification screenshot](synology-specs.webp)

CPU scores and sample counts from the comparison follow. These measure CPU performance, not the NAS as a whole; the R1600 result has only nine samples.

| Metric | DS918+: J3455 | DS720+: J4125 | DS923+: R1600 |
| --- | ---: | ---: | ---: |
| Single-thread score | 812 | 1,151 | 1,721 |
| CPU Mark multi-thread score | 2,236 | 2,926 | 3,264 |
| Relative single-thread performance (DS918+ = 1) | 1.00 | 1.42 | 2.12 |
| Relative multi-thread performance (DS918+ = 1) | 1.00 | 1.31 | 1.46 |
| Aggregated sample count | 546 | 690 | 9 |
{.wide .expand}

| Upgrade | Single-thread gain | Multi-thread gain | Interpretation |
| --- | --- | --- | --- |
| DS918+ → DS720+ | About 42% | About 31% | Clear CPU improvement, but half as many drive bays |
| DS720+ → DS923+ | About 50% | About 12% | Large single-thread gain; modest multi-thread gain |
| DS918+ → DS923+ | About 112% | About 46% | Roughly twice the single-thread performance, not twice the multi-thread performance |
{.wide .expand}

[Original CPU-score screenshot](synology-scores.webp)

The newer crop of NAS boxes—whether from Synology, Beelink, or Minisforum—finally ships with usable CPU performance. The Ryzen 7 H 255 is an 8-core, 16-thread Zen 4 chip, which is plenty capable of running real workloads alongside storage.

![Observed logical topology of the ME Pro, including the Ryzen 7 255, three NVMe drives, four hard drives, 10GbE NIC, and storage mounts](topology.webp)

### What the topology snapshot shows

The diagram reconstructs the logical topology of the connected devices, with links cross-checked through PCI, sysfs, and SMART. It does not map motherboard wiring or empty slots. It shows three connected NVMe drives; the machine has four physical M.2 slots. Each ASMedia controller serves two hard drives, with no USB storage bridge.

| Component | Observed configuration |
| --- | --- |
| CPU | Ryzen 7 255; 8 cores / 16 threads |
| Graphics | Radeon 780M |
| Memory | 32 GiB dual-channel DDR5-5600 |
| 10GbE | Realtek RTL8127; PCIe 4.0 ×1 |

| Device or controller | Link and device | Mounts, pool, or other observed role |
| --- | --- | --- |
| P310 500 GB | 06:00.0, PCIe 4.0 ×4 | `/` (system) and `/boot/efi` |
| Samsung 970 PRO 1 TB | 04:00.0, PCIe 3.0 ×4 | `/data`; PostgreSQL data and WAL |
| Samsung 970 EVO 2 TB | 01:00.0, PCIe 3.0 ×4 | `/data2`; cumulative media errors: 74 |
| ASMedia AHCI at 03:00.0 | PCIe 3.0 ×1; two SATA 6 Gb/s ports | IronWolf 16 TB `sda` at `/data5` and IronWolf 16 TB `sdb` at `/data6`; both 7,200 rpm / 512e. The screenshot displays 99.17%, but does not label what that number measures. |
| ASMedia AHCI at 05:00.0 | PCIe 3.0 ×1; two SATA 6 Gb/s ports | Two HGST 4 TB drives, `sdc` and `sdd`; both are `md8` members, 7,200 rpm / 512e. The two-drive stripe is md8 RAID 0 at `/d8`, with no redundancy. |
| Realtek RTL8127 10GbE | PCIe 4.0 ×1 | Network interface |
{.wide .expand}

The diagram shows the 16 TB drives mounted separately; the storage layout described below groups them into a RAID 0 pool.

| Metric | Observed value | Scope and limitation |
| --- | --- | --- |
| SHA-256 scaling | 16 processes versus one: 14.10× | This applies only to the fixed SHA-256 workload used for the test. |
| Installed raw capacity | 43.528 TB / 39.589 TiB | Decimal TB and binary TiB express the same raw capacity. Formatted space, free space, and redundancy are separate quantities. |
| Network payload | 9.405 / 8.876 Gb/s for m3 → m4 / m4 → m3 | Separate runs using four TCP streams and receiver payload; this is not SMB or NFS file throughput. |
{.wide .expand}

### Local hardware audit of the Ryzen 7 255 platform

DMI identifies the machine as an AZW ME Pro, and Linux reports `AMD Ryzen 7 255 w/ Radeon 780M Graphics`. The full audit below distinguishes detected hardware, published specifications, and features that have yet to be tested.

<details>
<summary>Full hardware inventory: CPU, memory, graphics, networking, and system state</summary>

Beelink lists H 255, N95, and N150 as distinct models and identifies AZW as its parent company. The ME Pro platform announced on May 28, 2026 includes two- and four-HDD versions and 10GbE. Four native SATA HDDs, 10GbE, and SO-DIMMs strongly match the H 255 four-bay model, although an SSH inspection cannot establish the enclosure's appearance or identify empty slots. The audit excludes specifications, photos, and power figures from the older N95/N150 two-bay model.

Reference labels follow the original hardware report.

#### Identity, CPU, and virtualization

| Audit item | Observed result | Evidence and limits |
| --- | --- | --- |
| System identity | AZW ME Pro; family ME / V1.0; motherboard AZW ME Pro; DMI chassis Desktop; serial `CH2556KG40214` | SSH confirmed [E01]. |
| Processor | AMD Ryzen 7 255 with Radeon 780M Graphics; 1 socket; 8 cores; 16 threads; 1 NUMA node; FP8 | SSH confirmed [E01]. |
| Architecture and specifications | Zen 4 / Hawk Point / TSMC 4 nm; base 3.8 GHz; maximum boost 4.9 GHz; default TDP 45 W; cTDP 35–54 W; Tjmax 100°C | Official CPU specifications [S01]. |
| Cache and instructions | L1D 256 KiB + L1I 256 KiB (8 instances each); L2 8 MiB; L3 16 MiB; AES / SHA / AVX2 / AVX-512 / SVM / NPT | Kernel exposed [E01]. |
| Virtualization and isolation | AMD-V, AMD-Vi, interrupt remapping; 39 IOMMU groups; disks and NIC in separate groups | Enumerated features [E01]; KVM x2AVIC firmware limitation notice. Device passthrough was not validated. |
| Current CPU policy | `amd_pstate` active / `amd-pstate-epp`; powersave + balance_performance; boost enabled; policy range 1.115–4.967 GHz | This is a policy snapshot, not sustained measured frequency. [E01] |
| CPUID and microcode | Family 25 / Model 117 / Stepping 2; microcode `0x0a70520a` | SSH confirmed [E01]. |
{.wide .expand}

#### Memory and graphics

| Audit item | Observed result | Evidence and limits |
| --- | --- | --- |
| Installed memory | 2 × 16 GiB Micron / Crucial `CT16G56C46S5.C8D`; P0 CHANNEL A / B; DDR5 SO-DIMM, single-rank, unbuffered, 1.1 V; serials `52FD855E` / `52FD84F5` | DMI and driver confirmed [E01]. |
| Memory speed and visible capacity | Configured and rated 5600 MT/s; dual-channel / 128-bit data width; installed 32 GiB; Linux `MemTotal` 30.129 GiB; baseline available 28.311 GiB; swap 8 GiB | SSH confirmed [E01]. |
| ECC and upgrade limit | Local DMI: ECC None; AMD CPU specifications explicitly say ECC unsupported. DMI motherboard table reports a 64 GB maximum; CPU specifications report 256 GB | These are different limits reported for the motherboard and CPU; actual high-capacity motherboard compatibility was not verified. [E01] [S01] |
| GPU and media engine | Radeon 780M; kernel active CU 12; gfx 11.0 / VCN 4.0 / JPEG 4.0; SCLK levels 800 / 1100 / 2600 MHz; `amdgpu` / DRM 3.64.0; Mesa 26.0.8 | Driver initialized [E01]. |
| Shared graphics memory | Fixed UMA VRAM 512 MiB; GTT about 15.06 GiB | GTT is an addressable shared system-memory pool, not dedicated VRAM or a permanently allocated region. Actual graphics, VA-API, and transcoding performance were not tested. [E01] |
| GPU firmware | VBIOS `113-PHXGENERIC-001`; SMC 76.94.0; VCN ENC 1.24 / DEC 9 / revision 16; all display connectors disconnected | SSH confirmed [E01]. |
{.wide .expand}

#### Network, I/O, and system state

| Audit item | Observed result | Evidence and limits |
| --- | --- | --- |
| 10GbE | Realtek RTL8127A / `10ec:8127` rev05; 07:00.0 / PCIe 4.0 ×1; `enp7s0` / 10000 Mb/s Full; `r8169`, `rtl8127a-1_0.0.5`; MTU 1500; RX/TX ring 256; pause off; EEE enabled/inactive | Link and throughput measured [E01] [E04]. |
| 2.5GbE | Realtek RTL8125D / `10ec:8125` rev0c; 02:00.0 / PCIe 2.0 ×1; `enp1s0` has no carrier; `r8169`, `rtl8125d-2_0.0.4` | Enumerated, but no link; throughput not tested. [E01] |
| Wireless and Bluetooth | MediaTek `14c3:7920` / AzureWave `1a3b:6471`; 08:00.0 / PCIe 1.0 ×1; `mt7921e`; firmware `20260224110939`; `wlp8s0` down. Bluetooth `13d3:3621` over USB / 480 Mb/s | Wireless generation and throughput were not verified. Enumerated; wireless untested. [E01] |
| USB and USB4 | Logitech `046d:c52b` receiver; USB SuperSpeed root 10000M; on-chip USB4/Thunderbolt initialized; no USB4 device connected; no USB mass-storage bridge | Actual port speed was not verified. [E01] |
| Audio | Realtek ALC897 Analog plus four HDMI audio devices | Enumerated by ALSA as root. SSH confirmed [E01]. |
| BIOS and system | AMI A8HPT008 / 2026-08-21; BIOS Revision 5.29; SMBIOS 3.5.0 / UEFI; Ubuntu 26.04.1 LTS; kernel 7.0.0-38-generic; baseline uptime 1 day 43 minutes | SSH confirmed [E01]. |
| Services and status | `postgres`, `pgbouncer`, `haproxy`, `smbd`, exporters, `smartmontools`, `chrony`, `tailscaled`, and others running; failed units 0; baseline load 0.06 / 0.22 / 0.39 | Runtime snapshot [E01]. |
{.wide .expand}

[Original Ryzen 7 255 hardware-audit screenshot](h255.webp)

</details>

### Putting the CPU to work

Honestly, if I didn't already own the GTR9 Pro, I probably would have bought the Minisforum N5 Max with an AMD Ryzen AI Max 395/495 and let a single box handle both storage and heavy compute.

One natural use for a NAS with some CPU headroom is storing and browsing photos. Synology Photos is fairly limited; a self-hosted photo library on the level of Apple Photos needs some processing power. I run Immich for this. The catch is that it needs PostgreSQL with vector extensions. `pgvector` is still the foundation, and [the current Immich setup also uses VectorChord, which depends on it](https://docs.immich.app/administration/postgres-standalone/).

Most people would put together a Docker Compose setup. I do this for a living, so naturally I used my own stack: deploy PostgreSQL in one command with Pigsty, which I developed, then run Immich on top. My entire photo library lives there now. Here are the [English deployment docs](https://pigsty.io/docs/app/immich/); the [Chinese original](https://pigsty.cc/docs/app/immich/) is also available.

[Pigsty v4.4 Release](/en/pigsty/v4.4/): Immich support

![Chinese Pigsty documentation for deploying Immich with separately managed PostgreSQL](immich-docs.webp)

*The app layer runs through Docker Compose, while Pigsty manages PostgreSQL separately from the app's containers. VectorChord provides vector search. PostgreSQL stores metadata, and the filesystem holds originals and generated media; both need backups. Valkey/Redis handles queues and caching rather than the authoritative dataset.*

![Immich self-hosted photo library showing travel images dated September 14, September 13, and May 9, 2025](immich-library.webp)

## What Do I Actually Keep on a NAS?

Which brings us back to a basic question: what do you actually use a NAS for?

Most people treat a NAS as a private cloud drive for movies, photos, and raw footage. Video creators use them heavily because camera footage has to live somewhere, and my use case isn't much different.

My Synology DS923+ provides about 26 TB of capacity, just enough for all my data (roughly 25 TB after deduplication). With a complete, authoritative copy on the Synology, I skipped redundancy on the ME Pro and used RAID 0:

- **30 TB pool (two 16 TB HDDs):** stores copies of the files from the Synology, plus data that previously didn't fit;
- **8 TB pool (two 4 TB HDDs):** holds private-tracker datasets alongside video-editing footage and project files.

Its biggest payoff, though, is freeing up the 8 TB internal SSDs on both of my daily-driver Macs (an M1 Max and an M5 Max) so that flash storage can stay dedicated to coding work. Apple prices internal flash storage like solid gold; spinning rust in a NAS is a much better place for cold data.

### What the file index counts

![File index showing 51,707,108 entries, 45,914,984 regular files, and 68.43 TB of logical size including sparse-file holes](files.webp)

My unified SQLite index reports logical size, including sparse-file holes that count toward a file's length without occupying corresponding disk blocks. The 68.43 TB total therefore isn't physical disk usage or the NAS's usable capacity. The interface also provides a browsable capacity view, full report, data dictionary, query examples, and validation results.

| File-index metric | Value | Meaning |
| --- | ---: | --- |
| Total entries | 51,707,108 | Objects in the unified SQLite index |
| Regular files | 45,914,984 | Regular files among those entries |
| Logical size | 68.43 TB | Includes sparse-file holes; not physical stored usage or NAS usable capacity |
{.wide .expand}

## What's Next on the Hardware List?

I now have six computers on my home LAN. I'm glad I didn't sell the older ones secondhand. In the AI agent era, every one of them has found a second life.

I still have a couple of older systems sitting around that I've been thinking about repurposing:

1. An old X99 gaming rig with a 2019-era flagship CPU, 32 GB of RAM, and an RTX 2080 Ti.
2. A Dell PowerEdge R730 server with sixteen 16 GB ECC DIMMs (256 GB total), dual CPUs totaling 36 cores and 72 threads, and a 3.2 TB PCIe NVMe SSD.

Throwing those parts out would be a waste, and combining them could make a capable machine. The catch is noise and power draw. Right now, my entire rack plus monitor uses around 400 W in everyday operation and 700–800 W under full load. One of those big servers could draw that much by itself under load.

More importantly, my current setup is almost silent. The drives make a little noise during heavy reads and writes, but that doesn't bother me. The rack sits beside me and doubles as a space heater this time of year. Server fan noise, though, I couldn't live with.

I looked into rebuilding the old hardware as a quieter machine. Workstation towers from a decade ago, such as the Dell T7910 and HP Z840, looked like a good fit. I could buy one, move over the R730's two CPUs and 16 DIMMs, add the GPU and PCIe storage card, and perhaps play with some Intel Optane drives or a Micron X100. The good stuff from the enterprise scrap heap.

When I thought it through, though, I couldn't come up with a workload that actually needed that box.

If I'm being honest, there are only two machines I really want right now.

The first is a Mac Studio with an M5 Ultra and 512 GB of unified memory. That much memory would let me run models in the GLM-5, GLM-5.3, and GLM-5.3 Flash class locally at a reasonable speed, even uncensored models.

Some context: I already have Zhipu's v1 Max GLM Coding Plan, which costs next to nothing, plus ¥16,000 sitting in my Zhipu account, enough to cover years of subscriptions. I have plenty of quota, and the models are capable. Even with free credits, though, I wouldn't trust the cloud with work as personal as an assistant's; [what ZCode did was warning enough](/en/ai/zcode-upload/).

What I want is one box running an always-on, entirely local dispatcher with no usage limits: an assistant that assigns all the work and handles routine jobs itself. That will probably be my next computer.

The second machine would be a top-end AMD desktop paired with a serious GPU. If street prices on the RTX 5090 or RTX Pro 6000 ever come back down to earth, I'd love to pick one up. I'm still kicking myself for not buying a card a few months ago when pricing was reasonable.

The *Witcher 3* remaster just came out, with a new expansion, *The Witcher 4*, and other demanding games lined up. Running them on my old RTX 2080 Ti is painful. What I'd really love is a breakthrough in NVIDIA driver support on Apple Silicon, or a community hack, so I could plug an NVIDIA eGPU into a Mac or the GTR9 Pro and play on that.

Anyway, that is all for another day. Between the Synology DS923+ and the Beelink ME Pro, my storage setup is set for the next five years. I doubt I'll buy another NAS during that stretch; any storage tinkering from here on out will probably just be playing with old Intel Optane or Micron X100 drives.

## Closing Advice for NAS Buyers

That about covers it. To wrap up, a few practical takeaways if you are shopping for a NAS:

If you don't want to tinker and just want an appliance that works, Synology is still the best option. Its software is mature, the ecosystem is excellent, and installing or removing drives is smooth and entirely tool-free. But the markup is brutal: for the same money, you get an anemic CPU and 1GbE networking. It feels like an outright insult. Still, it does deliver reliability and peace of mind.

If you are willing to tinker a little, a machine like the Beelink ME Pro is well worth trying. It is really a PC NAS. For a conventional NAS setup, install fnOS. If you only need a storage server, have Codex handle the configuration details, then mount the shares on your own devices. That isn't especially difficult either.

As for me, I wanted both: a hands-off, near-enterprise appliance for my primary data, and an open box where I can tinker and run whatever open-source stack I like. Buying one of each solved the problem cleanly.

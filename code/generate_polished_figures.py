import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE_DIR, 'figures_polished')
os.makedirs(OUT, exist_ok=True)

# Global style
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'axes.linewidth': 0.8,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'savefig.dpi': 600,
})
GREEN = '#2ca02c'
GRAY = '#9aa1a8'
DARK_GRAY = '#6b6f73'
LIGHT_GRAY = '#d6d9dc'
BLUE = '#1f5fbf'
RED = '#bf1f1f'
BLACK = '#222222'

def finish(fig, name, tight=True):
    png = os.path.join(OUT, name + '.png')
    pdf = os.path.join(OUT, name + '.pdf')
    if tight:
        fig.savefig(png, bbox_inches='tight', pad_inches=0.03)
        fig.savefig(pdf, bbox_inches='tight', pad_inches=0.03)
    else:
        fig.savefig(png)
        fig.savefig(pdf)
    plt.close(fig)

# Figure 1: framework diagram
fig, ax = plt.subplots(figsize=(8.8, 4.9))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
modules = [
    (0.13, 0.75, 'TGM\nTruncated-Gaussian\nMechanism\ntarget-budget calibration'),
    (0.38, 0.75, 'ECP\nEnergy &\nAR-prediction\nCo-process'),
    (0.63, 0.75, 'ACG\nAdaptive\nConsensus Gain'),
    (0.87, 0.75, 'AET\nAdaptive Event-Triggered\ncommunication'),
]
for x,y,text in modules:
    w,h=0.20,0.17
    box=FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.02,rounding_size=0.02',
                       edgecolor=BLUE,facecolor='#f7fbff',linewidth=1.4)
    ax.add_patch(box)
    lines=text.split('\n')
    ax.text(x,y+0.045,lines[0],ha='center',va='center',fontsize=12,fontweight='bold',color=BLACK)
    ax.text(x,y-0.02,'\n'.join(lines[1:]),ha='center',va='center',fontsize=8.5,color=BLACK)
node_positions=[(0.22,0.36,'Node $i$'),(0.50,0.36,'Node $j$'),(0.78,0.36,'Node $k$')]
for x,y,text in node_positions:
    w,h=0.15,0.10
    box=FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.02,rounding_size=0.015',
                       edgecolor=BLACK,facecolor='#f1f1f1',linewidth=0.9)
    ax.add_patch(box)
    ax.text(x,y,text,ha='center',va='center',fontsize=12,color=BLACK)
# module arrows
arrow_kw=dict(arrowstyle='-|>', mutation_scale=12, linewidth=1.2, color=BLUE)
for (sx,sy,_), (tx,ty,_) in [(modules[0],node_positions[0]),(modules[1],node_positions[1]),(modules[2],node_positions[1]),(modules[3],node_positions[2])]:
    ax.add_patch(FancyArrowPatch((sx, sy-0.10), (tx, ty+0.07), connectionstyle='arc3,rad=0.0', **arrow_kw))
# red node interactions
ax.add_patch(FancyArrowPatch((0.30,0.36),(0.42,0.36), arrowstyle='<->', mutation_scale=13, linewidth=1.2, color=RED))
ax.text(0.36,0.405,'event-triggered\nrelease',ha='center',va='bottom',fontsize=8.5,color=RED,fontweight='bold')
ax.add_patch(FancyArrowPatch((0.58,0.36),(0.70,0.36), arrowstyle='<->', mutation_scale=13, linewidth=1.2, color=RED))
ax.text(0.64,0.405,'AR prediction\nduring silence',ha='center',va='bottom',fontsize=8.5,color=RED,fontweight='bold')
ax.text(0.50,0.14, '$\\bf{Core\\ loop:}$ sparse triggering $\\rightarrow$ larger event-level target budget $\\rightarrow$ lower value-channel noise\n$\\rightarrow$ better AR prediction $\\rightarrow$ continued sparse triggering',
        ha='center',va='center',fontsize=9.2,color=BLACK)
finish(fig,'framework_architecture')

# Figure 2: closed-loop mechanism
fig, ax = plt.subplots(figsize=(8.2, 4.2))
ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
box_specs = {
    'sparse': (0.18,0.78,0.26,0.10,'Sparse triggering'),
    'eps': (0.50,0.78,0.26,0.10,r'Per-release $\varepsilon_{tx}$ increases'),
    'sigma': (0.82,0.78,0.22,0.10,r'$\bar{\sigma}$ decreases'),
    'snr': (0.82,0.48,0.28,0.10,'AR input SNR improves'),
    'nu': (0.50,0.48,0.22,0.10,r'$\nu_0$ decreases'),
    'gamma': (0.22,0.48,0.22,0.10,r'$\Gamma$ decreases'),
    'mse': (0.22,0.22,0.22,0.10,'MSE decreases'),
}
for x,y,w,h,text in box_specs.values():
    box=FancyBboxPatch((x-w/2,y-h/2),w,h,boxstyle='round,pad=0.02,rounding_size=0.02',edgecolor=BLUE,facecolor='#fbfdff',linewidth=1.3)
    ax.add_patch(box); ax.text(x,y,text,ha='center',va='center',fontsize=11,color=BLACK)
arr=dict(arrowstyle='-|>',mutation_scale=13,linewidth=1.2,color=BLUE)
def edge(k, side):
    x,y,w,h,_ = box_specs[k]
    if side=='R': return (x+w/2,y)
    if side=='L': return (x-w/2,y)
    if side=='T': return (x,y+h/2)
    if side=='B': return (x,y-h/2)
for start_key,start_side,end_key,end_side in [
    ('sparse','R','eps','L'),('eps','R','sigma','L'),('sigma','B','snr','T'),
    ('snr','L','nu','R'),('nu','L','gamma','R'),('gamma','B','mse','T')]:
    ax.add_patch(FancyArrowPatch(edge(start_key,start_side),edge(end_key,end_side),**arr))
# dashed feedback path with clean right-angle segments
x_left=0.06
x_mse_left,y_mse= edge('mse','L')
x_sparse_left,y_sparse= edge('sparse','L')
ax.plot([x_mse_left,x_left,x_left,x_sparse_left],[y_mse,y_mse,y_sparse,y_sparse], color=BLUE, lw=1.2, ls='--')
ax.add_patch(FancyArrowPatch((x_sparse_left-0.015,y_sparse),(x_sparse_left,y_sparse),arrowstyle='-|>',mutation_scale=13,linewidth=1.2,color=BLUE,linestyle='--'))
finish(fig,'closed_loop_mechanism')

# Figure 3: theoretical trade-off boundary curve (consistent with Eq. 26)
delta = np.linspace(0.0,0.985,260)
base = 1.0
curv = 0.18*(delta/(1-delta+1e-9))**2 + base
# normalize to 1 at delta=0
fig, ax = plt.subplots(figsize=(5.6,3.7))
ax.plot(delta,curv,color=GREEN,linewidth=2.0,label='Eq. (26) trend')
ax.axvspan(0.86,0.94,color=GREEN,alpha=0.12,label='practical sparse region')
ax.axvspan(0.97,0.985,color=RED,alpha=0.10,label='near-divergence region')
ax.set_yscale('log')
ax.set_xlim(0,0.985)
ax.set_xlabel(r'Communication-saving ratio $\delta_E$')
ax.set_ylabel('Normalized MSE upper envelope (log)')
ax.grid(True,which='both',linestyle='--',alpha=0.28)
ax.annotate('more sparse\ncommunication',xy=(0.88,3.5),xytext=(0.55,11),arrowprops=dict(arrowstyle='->',color=DARK_GRAY,lw=1.0),fontsize=8,color=DARK_GRAY)
ax.annotate('error grows when\ncommunication vanishes',xy=(0.975,curv[-1]),xytext=(0.58,80),arrowprops=dict(arrowstyle='->',color=RED,lw=1.0),fontsize=8,color=RED)
ax.legend(loc='upper left',frameon=True,framealpha=0.95)
for spine in ['top','right']:
    ax.spines[spine].set_visible(False)
finish(fig,'tradeoff_curve')

# Figure 4: ablation
methods = ['Full\nE-PAS','w/o AR','w/o\nbudget','w/o ACG','w/o\ndual-trig']
mse = np.array([0.00036,0.01285,0.00031,0.00033,0.00032])
err = np.array([0.00004,0.0018,0.00003,0.00004,0.00004])
comm = np.array([1890,6700,1865,1880,1875])
fig, axs = plt.subplots(1,2,figsize=(7.8,3.3))
colors=[GREEN]+[GRAY]*4
axs[0].bar(range(len(methods)),mse,yerr=err,color=colors,edgecolor='none',capsize=2)
axs[0].set_ylabel('Steady-state MSE')
axs[0].set_xticks(range(len(methods)),methods)
axs[0].set_title('(a) Accuracy (8 reps, controlled)',loc='left',fontweight='bold')
axs[0].grid(axis='y',linestyle='--',alpha=0.30)
axs[1].bar(range(len(methods)),comm,color=colors,edgecolor='none')
axs[1].set_ylabel('Communication count')
axs[1].set_xticks(range(len(methods)),methods)
axs[1].set_title('(b) Communication',loc='left',fontweight='bold')
axs[1].grid(axis='y',linestyle='--',alpha=0.30)
for ax in axs:
    for s in ['top','right']:
        ax.spines[s].set_visible(False)
fig.tight_layout(w_pad=2.0)
finish(fig,'controlled_ablation')

# Figure 5: budget fairness
names = ['Periodic','Std. ET','Priv.-aware','E-PAS']
comm = np.array([15000,6814,12863,1218])
per = 1.0/comm
mult = np.array([12.3,5.6,10.6,1.0])
fig, axs = plt.subplots(1,3,figsize=(9.7,3.1))
for ax, vals, title, ylabel in zip(
        axs,
        [comm, per, mult],
        ['(a) Communication count','(b) Per-event budget','(c) Matched-noise budget multiplier'],
        ['Communication count',r'$\varepsilon_{tx}=\varepsilon_g/T$','Global budget multiplier']):
    ax.bar(range(4), vals, color=[GRAY,GRAY,GRAY,GREEN], edgecolor='none')
    ax.set_xticks(range(4),names,rotation=20,ha='right')
    ax.set_title(title,loc='left',fontweight='bold')
    ax.set_ylabel(ylabel)
    ax.grid(axis='y',linestyle='--',alpha=0.30)
    for s in ['top','right']:
        ax.spines[s].set_visible(False)
for i,v in enumerate(mult):
    axs[2].text(i,v+0.25,f'{v:.1f}x',ha='center',va='bottom',fontsize=8)
fig.tight_layout(w_pad=2.0)
finish(fig,'budget_fairness_accounting')

# Figure 6: parameter sensitivity
p = np.array([1,2,3,4,5])
p_mse = np.array([0.000354,0.000360,0.000327,0.000311,0.000350])
p_comm = np.array([1856,1864,1884,1888,1901])
rho = np.array([0.1,0.2,0.4,0.6,0.7])
r_mse = np.array([0.00027,0.00029,0.00033,0.00045,0.00120])
r_comm = np.array([1890,1893,1897,1900,2005])
K = np.array([8,12,16,20,24])
k_mse = np.array([0.00053,0.00026,0.00028,0.00032,0.00030])
k_comm = np.array([2420,1985,1975,1965,1950])
B = np.array([0.1,0.25,0.50,1.00])
b_mse = np.array([0.000245,0.000270,0.000310,0.000370])
b_comm = np.array([1845,1875,1888,1890])
series = [
    (p,p_mse,p_comm,'(a) Predictor order $p$','AR order $p$'),
    (rho,r_mse,r_comm,'(b) Budget step $\\rho_b$','Budget step $\\rho_b$'),
    (K,k_mse,k_comm,'(c) Timeout $K_{max}$','Timeout $K_{max}$'),
    (B,b_mse,b_comm,'(d) Truncation bound $B$','Truncation bound $B$'),
]
fig, axs = plt.subplots(2,2,figsize=(8.0,5.8))
handles=[]
for ax,(x,y1,y2,title,xlabel) in zip(axs.flatten(),series):
    l1=ax.plot(x,y1,'o-',color=GREEN,lw=1.6,ms=4.5,label='Steady-state MSE')
    ax.set_ylabel('Steady-state MSE',color=GREEN)
    ax.tick_params(axis='y',labelcolor=GREEN)
    ax.set_xlabel(xlabel)
    ax.set_title(title,loc='left',fontweight='bold')
    ax.grid(True,linestyle='--',alpha=0.28)
    ax2=ax.twinx()
    l2=ax2.plot(x,y2,'s--',color=DARK_GRAY,lw=1.4,ms=4,label='Communication')
    ax2.set_ylabel('Communication',color=DARK_GRAY)
    ax2.tick_params(axis='y',labelcolor=DARK_GRAY)
    for s in ['top']:
        ax.spines[s].set_visible(False); ax2.spines[s].set_visible(False)
    handles = [l1[0],l2[0]]
fig.legend(handles,['Steady-state MSE','Communication'],loc='lower center',ncol=2,frameon=False,bbox_to_anchor=(0.5,-0.01))
fig.tight_layout(rect=(0,0.06,1,1),h_pad=1.6,w_pad=2.0)
finish(fig,'parameter_sensitivity_scan')

# Figure 7: supplemental scans
fig, axs = plt.subplots(1,2,figsize=(7.8,3.2))
axs[0].plot(p,p_mse,'o-',color=GREEN,lw=1.8,ms=5)
axs[0].set_title('(a) Order $p$ scan',loc='left',fontweight='bold')
axs[0].set_xlabel('Predictor order $p$')
axs[0].set_ylabel('Steady-state MSE')
axs[0].grid(True,linestyle='--',alpha=0.28)
axs[1].plot(rho,r_mse,'o-',color=GREEN,lw=1.8,ms=5)
axs[1].set_title('(b) Budget step $\\rho_b$ scan',loc='left',fontweight='bold')
axs[1].set_xlabel('Budget step size $\\rho_b$')
axs[1].set_ylabel('Steady-state MSE')
axs[1].grid(True,linestyle='--',alpha=0.28)
for ax in axs:
    for s in ['top','right']:
        ax.spines[s].set_visible(False)
fig.tight_layout(w_pad=2.0)
finish(fig,'supplemental_parameter_scans')

# Figure 8 trigger rate
cats = ['ER ideal','ER privacy','WS privacy']
meas = np.array([0.062,0.078,0.100])
timeout = np.array([0.05,0.05,0.05])
envelope = np.array([0.38,0.57,0.88])
x=np.arange(len(cats)); width=0.22
fig, ax = plt.subplots(figsize=(5.8,3.7))
ax.bar(x-width,meas,width,label='Measured trigger rate',color=GREEN,edgecolor='none')
ax.bar(x,timeout,width,label=r'Timeout floor $1/K_{max}$',color=DARK_GRAY,edgecolor='none')
ax.bar(x+width,envelope,width,label='Quasi-stationary envelope',color=LIGHT_GRAY,edgecolor='none')
ax.set_ylabel('Per-node trigger rate')
ax.set_xticks(x,cats)
ax.set_ylim(0,1.0)
ax.grid(axis='y',linestyle='--',alpha=0.30)
ax.legend(loc='upper left',frameon=True,framealpha=0.95)
for s in ['top','right']:
    ax.spines[s].set_visible(False)
finish(fig,'trigger_rate_validation')

# Figure 9 AR residual
h=np.arange(1,20)
res=np.array([0.0198,0.0200,0.0198,0.0190,0.0186,0.0182,0.0179,0.0176,0.0174,0.0172,0.0170,0.0169,0.0171,0.0172,0.0171,0.0168,0.0165,0.0162,0.0160])
fig, ax = plt.subplots(figsize=(5.8,3.7))
ax.plot(h,res,'o-',color=GREEN,lw=1.8,ms=4.5,label='Measured (50 reps)')
ax.set_xlabel('Silent prediction horizon (steps)')
ax.set_ylabel('Mean absolute AR residual')
ax.set_ylim(0,0.025)
ax.grid(True,linestyle='--',alpha=0.30)
ax.legend(loc='upper right',frameon=True,framealpha=0.95)
for s in ['top','right']:
    ax.spines[s].set_visible(False)
finish(fig,'ar_residual_growth')

# Also create a communication-accuracy scatter as supplementary, not used in main.
fig, ax = plt.subplots(figsize=(5.8,3.7))
xvals=np.array([15000,6814,12863,1218])
yvals=np.array([3.70e-3,5.04e-3,2.06e-3,1.43e-4])
labels=['Periodic','Standard ET','Privacy-aware','E-PAS']
colors=[GRAY,GRAY,GRAY,GREEN]
ax.scatter(xvals,yvals,s=[60,60,60,75],c=colors,edgecolor='k',linewidth=0.7,zorder=3)
for x0,y0,lab in zip(xvals,yvals,labels):
    dx=180 if lab!='E-PAS' else 260
    dy=1.05 if lab!='E-PAS' else 1.15
    ax.text(x0+dx,y0*dy,lab,fontsize=8,va='center')
ax.set_yscale('log')
ax.set_xlabel('Communication count (N=100, 150 steps)')
ax.set_ylabel('Steady-state MSE (log)')
ax.grid(True,which='both',linestyle='--',alpha=0.28)
ax.annotate('better',xy=(2000,2.0e-4),xytext=(4700,4.5e-4),arrowprops=dict(arrowstyle='->',lw=1.0,color=DARK_GRAY),fontsize=8,color=DARK_GRAY)
for s in ['top','right']:
    ax.spines[s].set_visible(False)
finish(fig,'supplemental_comm_accuracy_tradeoff')

print('Generated figures in', OUT)

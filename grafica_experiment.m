%Experiment Nitrogen
time = [0, 15, 20, 25, 30];
iHO  = [0.95, 0.1947, 0.1056, 0.0826, 0.0525];
iLO  = [0.05, 0.4537, 0.5225, 0.5427, 0.5650];
iGa  = [0.0, 0.1266, 0.1524, 0.1631, 0.1662];
iCO  = [0.0, 0.1572, 0.1898, 0.2042, 0.2138];
p = plot(time,iHO,'^', time, iLO,'^', time, iGa,'^', time, iCO,'^');

% %Experiment Air
% time = [0, 15, 20, 25, 30];
% iHO  = [0.95, 0.2978, 0.2334, 0.1621, 0.0964];
% iLO  = [0.05, 0.4078, 0.4397, 0.4685, 0.5036];
% iGa  = [0.0, 0.0912, 0.1296, 0.1401, 0.1498];
% iCO  = [0.0, 0.1717, 0.1893, 0.2098, 0.2203];
% p = plot(time,iHO,'^', time, iLO,'^', time, iGa,'^', time, iCO,'^');

xlabel('Reaction time [days]');
ylabel('Content [wt %] ');

p(1).MarkerSize = 8;
p(1).Color = '#0072BD';
p(2).MarkerSize = 8;
p(2).Color = '#D95319';
p(3).MarkerSize = 8;
p(3).Color = '#EDB120';
p(4).MarkerSize = 8;
p(4).Color = '#7E2F8E';

hold on
data = load('results(NITROGEN_FINAL).txt');
t  = data(:,2);
Ho = data(:,3);
Lo = data(:,4);
Gs = data(:,5);
CO = data(:,6);
% % m = plot(t,Ho,'-', t,Lo, '-', t,Gs, '-', t,CO, '-');
% m(1).LineWidth = 1.5;
% m(1).Color = '#0072BD';
% m(2).LineWidth = 1.5;
% m(2).Color = '#D95319';
% m(3).LineWidth = 1.5;
% m(3).Color = '#EDB120';
% m(4).LineWidth = 1.5;
% m(4).Color = '#7E2F8E';

%Interpolation
ti = linspace(min(t), max(t), 100);
Hoi= pchip(t, Ho, ti);
Loi= pchip(t, Lo, ti);
Gsi= pchip(t, Gs, ti);
COi= pchip(t, CO, ti);
d = plot(ti,Hoi,'-', ti,Loi, '-', ti,Gsi, '-', ti,COi, '-');
d(1).LineWidth = 1.5;
d(1).Color = '#0072BD';
d(2).LineWidth = 1.5;
d(2).Color = '#D95319';
d(3).LineWidth = 1.5;
d(3).Color = '#EDB120';
d(4).LineWidth = 1.5;
d(4).Color = '#7E2F8E';


legend(d, 'Heavy Oil', 'Light Oil', 'Gas', 'Coke');
legend('boxoff');

hold off
